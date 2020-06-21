# Week 3 into GSoC

Today (June 21, 2020) marks the ending of week 3 of GSoC coding period. Let me summarize what I did for this week. Following up the work done in [week 2](/gsoc/week-2-into-gsoc), I went on exploring `ArviZ` InferenceData and `tfp.vi` module to learn how to deal with shapes, convergence checks and optimizers.

- Adding a new axis to samples resolved the shape issues. By this, `number of chains` parameter is set to 1 and all the priors are handled perfectly.
- The convergence checks did not seem to work properly. (As pointed out by my mentor, we need to adjust window size).
- The default tensorflow optimizers also did not lead to convergence really well. Trying out the default values taken from PyMC3, I got really good results. This motivated me to write `updates` module for Variational Inference Interface.
- I applied inverse of bijectors to transformed parameters to match support in bounded space. But this approach is wrong. I need to handle this using deterministics callback which I will do in coming week.
- I had also written tests during this interval.
- From last week, I did not get quite good results while experimenting with Mean Field ADVI in TFP, PyMC3 and PyMC4. As suggested by my mentor, setting a common random seed and same optimizer leads to very good results . ([gist](https://gist.github.com/Sayam753/df2d11b6b5a1e875710656ecc013fad5))

## Experiments - [Source](https://gist.github.com/Sayam753/080a8daca8cadd30b350d7fb88cff293)

Whatever experiments I perform, I polish them out and share through GitHub gists. I do not why but I started loving to share code through GitHub gists rather than Colab or GitHub repo.

Here is the notebook -

<script src="https://gist.github.com/Sayam753/080a8daca8cadd30b350d7fb88cff293.js"></script>

## Tasks for week 4

Phase 1 Evaluations are coming up. So, I need to sync work with my proposed timeline and spend time summarizing all the results in a single notebook. My tasks for week 4 -

- Write tests for conjugate normal models with known mean/variance.
- Configure `atol` argument for `np.testing.assert_allclose`. (I misunderstood how this parameter works)
- Complete docs for optimizers by adding `**kwargs` option and writing corresponding maths equations.
- Properly configure convergence checks and add an example to quickstart notebook.
- Configure autobatching. (I need to understand how this works for mcmc)
- Integrate Deterministics callbacks.
- Complete Full Rank/Low Rank Approximation. (This will take time)
- Configure Minibatches.
- Update quick_start notebook with respect to all changes above.

### Extra

If I will be able to complete above mentioned tasks in time, I would love to -

- Have another implementation of Mean Field ADVI using `tfd.MultivariateNormalDiag`.
- Play around with Mean Field ADVI on Eight Schools notebook.
- Resolve a warning from `tfp.vi` module regarding repetitive use of `tf.function` in a loop. Maybe using `tf.while_loop` will solve this but I am not sure.
- Experiment with MeanField/ FullRank/ LowRank ADVI in TFP, PyMC3, PyMC4 inspired from [ColCarroll](https://github.com/ColCarroll)'s [notebook](https://nbviewer.jupyter.org/gist/ColCarroll/d673a3af7169bd713bcbdb9445d4a543). I am already getting excited to play around with this after having all APIs set correctly.

### For Evaluations

I look forward to learn how Variational AutoEncoders are implemented in PyMC3 and try implementing that in PyMC4.

I am thankful to my mentor for his constant guidance and pymc-devs for being such a supportive community.

!!! note ""
    Thank you for reading!

With :heart:,
Sayam
