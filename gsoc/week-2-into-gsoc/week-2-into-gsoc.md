# Week 2 into GSoC

Following up the work done in [week 1](/gsoc/week-1-into-gsoc), I started exploring surrounding packages of PyMC4 i.e. TFP, ArviZ and PyMC3 to gain better insights how things need to be integrated. On the way, I opened a few issues and PRs fixing docstrings.

- ArviZ Issue [#1232](https://github.com/arviz-devs/arviz/issues/1232) regarding rendering of notebooks.
- PyMC4 Issue [#283](https://github.com/pymc-devs/pymc4/issues/283) regarding Transformations. I am still wondering whether the transformations are missing or automatically handled.
- TFP PR [#965](https://github.com/tensorflow/probability/pull/965) that fixes `tfb.Chain` docstrings.

## Work done this week

Figuring out the solutions over the review of the PR [#280](https://github.com/pymc-devs/pymc4/pull/280), I have -

- Added `sample` method for sampling from posterior distribution.
- Fixed return type from `fit` function to include `Approximation` as well.
- Updated variational quickstart notebook incorporating both of the changes above.

It took me a bit longer to look out for good variable names and to make quick-start notebook similar to PyMC3's Variational API [notebook](https://docs.pymc.io/notebooks/variational_api_quickstart.html). But the time was worth it.

## Experiments

Most of the time this week, I spent experimenting on ideas building on top of week 1's work. I polished out my experiments and created two gists.

### Gist 1 - [Source](https://gist.github.com/Sayam753/df2d11b6b5a1e875710656ecc013fad5)

Comparison between MeanField ADVI in TFP, PyMC3 and PyMC4. It was fun doing this.

<script src="https://gist.github.com/Sayam753/df2d11b6b5a1e875710656ecc013fad5.js"></script>

### Gist 2 - [Source](https://gist.github.com/Sayam753/36bf35c482b705545eecb5353a8f8f6a)

Experimenting with ArviZ. I started learning from how trace from `tfp.mcmc.sample_chain` gets converted to ArviZ InferenceData. Following the same, I soon ran into shape issues while integrating it into `sample` method. I plan to resolve it in week 3.

<script src="https://gist.github.com/Sayam753/36bf35c482b705545eecb5353a8f8f6a.js"></script>

## Tasks for week 3

- Tests about convergence checks
- Add convergence criteria example in quick start notebook
- Include samples for untransformed variables as well
- Handle shape issues with ArviZ while sampling
- More user friendly optimizers

I am thankful to my mentor for his constant guidance and pymc-devs for being such a supportive community.

!!! note ""
    Thank you for reading!

With :heart:,
Sayam
