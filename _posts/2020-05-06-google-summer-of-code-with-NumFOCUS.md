---
title: GSoC'20 with NumFOCUS
categories: [Open Source]
tags: [GSoC, PyMC]
---

I am super excited to say that I have been selected as a Google Summer of Code student by NumFOCUS for PyMC4. I would like to thank my mentors [Thomas Wiecki](https://github.com/twiecki) and [Maxim Kochurov](https://github.com/ferrine) and the entire NumFOCUS community for giving this opportunity.

My project is about adding `Variational Inference Interface` to [PyMC4](https://github.com/pymc-devs/pymc4). Variational Inference scales better over larger datasets as compared to the traditional MCMC algorithms. First, I had plans to implement OPVI[^OPVI_paper] framework as done in PyMC3 this summer. But as corrected by my mentor [Maxim Kochurov](https://github.com/ferrine), it would have taken extra time and more debugging because of the difficulty to deal with `symbolic graph manipulations` in [Tensorflow](https://www.tensorflow.org/). Now, the whole plan is to implement two Variational Inference Algorithms - Mean Field ADVI[^ADVI_paper] and Full Rank ADVI[^ADVI_paper] in PyMC4. Mean Field ADVI posits a Spherical Gaussian family and Full Rank ADVI posits a Multivariate Gaussian family to minimize [KL divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence). I will write a blog post upto next week explaining both these algorithms.

All in all, I look forward to a great summer.
{: .notice--info}

[^OPVI_paper]: [Operator Variational Inference](https://arxiv.org/abs/1610.09033) Rajesh Ranganath, Jaan Altosaar, Dustin Tran, David M. Blei (2016)
[^ADVI_paper]: [Automatic Differentiation Variational Inference](https://arxiv.org/abs/1603.00788) Alp Kucukelbir, Dustin Tran, Rajesh Ranganath, Andrew Gelman, David M. Blei (2016).
