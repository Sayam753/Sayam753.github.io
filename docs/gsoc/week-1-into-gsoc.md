# Week 1 into GSoC

This blog contains my 1st week's progress (June 1 - June 7) into GSoC. After I have got a fair intuition of how [tfp.vi](https://www.tensorflow.org/probability/api_docs/python/tfp/vi) module works, I started implementing Mean Field ADVI in PyMC4. With the guidance of my mentor [Maxim Kochurov](https://github.com/ferrine), we have split the implementation of VI approximations into 3 major parts -

1. Vector LogProb function
2. Approximate Distribution from TFP
3. Integrate with TFP, Optimizers, etc

I started implementing ideas into my fork. Within 4-5 days, I have come up with a reasonable design incorporating the above 3 guidelines. And here is the PR [#280](https://github.com/pymc-devs/pymc4/pull/280) and now, I am working on the suggestions to improve API design.

On the way of my exploration of [tfp.vi](https://www.tensorflow.org/probability/api_docs/python/tfp/vi) module, I see that we can use either [tfp.distributions.JointDistributionSequential](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/JointDistributionSequential?version=nightly) or [tfp.distributions.MultivariateNormalDiag](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/MultivariateNormalDiag?version=nightly) to implement Mean Field ADVI. The PR #280 is based on JointDistributionSequential. I will incorporate use of MultivariateNormalDiag after having a flattened view of parameters.

I observe that I am a week ahead of my proposed GSoC timeline. This means I have more time to explore PyMC4.

Thank you for reading!

With :heart:,
Sayam
