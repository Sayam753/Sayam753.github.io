# Week 4 into GSoC

So, the phase 1 coding period ends and let me summarize what I did for the last week. Let's bring back the tasks proposed at the end of [week 3](/gsoc/week-3-into-gsoc) and figure out how many I have completed -

- [X] Write tests for conjugate normal models with known mean/variance.
- [X] Configure `atol` argument for `np.testing.assert_allclose`.
- [X] Complete docs for optimizers by adding `**kwargs` option and writing corresponding maths equations.
- [ ] Properly configure convergence checks and add an example to quickstart notebooks.
- [ ] Configure autobatching.
- [X] Integrate Deterministics callbacks. (But I did it wrong)
- [ ] Complete remaining Approximations.
    - [X] Full Rank Approximation.
    - [ ] Low Rank Approximation.
- [ ] Configure Minibatches.
- [X] Update quick_start notebook with respect to all changes above.

I was unable to complete a few tasks because I got stuck for many days figuring out how to correctly handle shapes in Full Rank ADVI. Finally I was able to come up with a new `_build_logfn` to handle shapes (on the guidelines provided by my mentor).

## Experiments

### Gist 1 - [Source](https://gist.github.com/Sayam753/130f91ae60175ba277a4b358575eac75)

I started the fourth week with a plan to include deterministics callbacks. Here are my experiments doing the same with PyMC4. All the determinitics are included in trace function. But when I opted for the same strategy to include deterministics while sampling, I got many shapes errors. The reason `determinitics_callback` failed because it assumes `sample size = 1`. We need to change this API.

<script src="https://gist.github.com/Sayam753/130f91ae60175ba277a4b358575eac75.js"></script>

### Gist 2 - [Source](https://gist.github.com/Sayam753/4e10b6a62da994470a245f843b9ef648)

My experiments involving how to configure Full Rank ADVI in TFP.

<script src="https://gist.github.com/Sayam753/4e10b6a62da994470a245f843b9ef648.js"></script>

### Gist 3 - [Source](https://gist.github.com/Sayam753/23592188b951bdeb53029eb0c4f4f2c3)

Comparisons drawn between PyMC3 and PyMC4 for 2-d Gaussians. TODO - complete comparisons for Mixture Distributions as well.

<script src="https://gist.github.com/Sayam753/23592188b951bdeb53029eb0c4f4f2c3.js"></script>

## Tasks for the remaining GSoC period

From the API point of view, only 5 tasks are left for the GSoC -

- Configure autobatching.
- Configure Minibatches.
- Add an option of progressbar.
- Include deterministics samples.
- Add convergence checks.

From the view of adding examples, all the notebooks from PyMC3 need to be ported to PyMC4.

For week 5, I look forward to add progressbar and convergence checks to PyMC4.

## Comparing with timeline

I have already completed all the tasks proposed for phase 1 evaluations. Also I have added Mean Field and Full Rank Approximations which were proposed for phase 2 and phase 3 of GSoC coding period respectively.

I am thankful to my mentor for his constant guidance and pymc-devs for being such a supportive community.

!!! note ""
    Thank you for reading!

With :heart:,
Sayam
