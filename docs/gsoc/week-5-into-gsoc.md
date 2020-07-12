# Week 5 into GSoC

Today (July 12, 2020) marks mid-way between phase 1 and phase 2 of GSoC coding period. Some good news, I have cleared Phase 1 evaluations. My mentor [Maxim Kochurov](https://github.com/ferrine) is amazing. Not only we explore different ideas related to the project but also we have great conversations not related to GSoC.

Most of the time spent this week was into resolving issues with Full Rank ADVI PR [#289](https://github.com/pymc-devs/pymc4/pull/289). Here is the long story short -

- Mean Field ADVI PR uses JointDistributionSequential and on the same paths, I added an interface of Full Rank ADVI.
- That approach was wrong because I misunderstood model flattening as variable flattening. And this leads to all sort of shape issues.
- After learning about model flattening, I integrated it into the PR.
- ADVI worked but losses contains lots of nans. As suspected, it was due to missing transformations.
- It took time to figure out how to setup transformations but later selected manually doing it.
- I was unable to make transformations generalized enough. Conditional statements and `tf.cond` does not seem to work either because at hand, we do not have values to transform inside bijectors. Later I plan to write a proposal mentioning the issue to PyMC-devs.
- Then after transformations, the **major** issue was of cholesky decomposition failure. And this [comment](https://github.com/ICL-SML/Doubly-Stochastic-DGP/issues/9#issuecomment-371167725) is a life saviour one.
- It took time to experiment with each option with park_bias_model and the last one worked. As stated, cholesky decomposition is unstable to `tf.float32`. So casting all the parameters to `tf.float64` resolved the issue. I also want to thank [Tirth Patel](https://twitter.com/__tirthap__) for helping me on the way to resolve dtype issues.
- Finally, I am all set to see the Full Rank ADVI PR getting merged.

## Experiments

### Gist 1 - [Source](https://gist.github.com/Sayam753/cc5126279932cffd65064bdc44754c2a)

Flattening and Full Rank ADVI in PyMC4

<script src="https://gist.github.com/Sayam753/cc5126279932cffd65064bdc44754c2a.js"></script>

### Gist 2 - [Source](https://gist.github.com/Sayam753/1a014bbc1afcf4dea0bb5e946e2e103f)

Testing issues with transformations

<script src="https://gist.github.com/Sayam753/1a014bbc1afcf4dea0bb5e946e2e103f.js"></script>

### Gist 3 - [Source](https://gist.github.com/Sayam753/50a1966172ed712d3974d007280fb0ae)

Failed at an attempt to generalize transformations

<script src="https://gist.github.com/Sayam753/50a1966172ed712d3974d007280fb0ae.js"></script>

### Experiment 4

Good news regarding the progress bars but I cannot do `tf.print("."*trace.step)`

```python
num_steps = 10_000
def trace_fn(trace):
    tf.cond(
        tf.math.mod(trace.step, 100) == 0,
        lambda: tf.print(trace.step, "/", num_steps, "Loss:", trace.loss),
        lambda: tf.print("", end="\r")
    )
    return trace.loss

# Pass this trace_fn to pm.fit()
```

I am planning to add convergence checks and progress bars for next week. Stay tuned.

I am thankful to my mentor for his constant guidance and pymc-devs for being such a supportive community.

!!! note ""
    Thank you for reading!

With :heart:,
Sayam
