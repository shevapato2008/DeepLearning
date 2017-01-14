from scipy.stats import norm

norm.pdf(0)                         # pdf of standard normal distribution, value when x = 0
norm.pdf(0, loc = 5, scale = 10)    # pdf of normal with mean = 5, stdDev = 10, value when x = 0

import numpy as np
r = np.random.randn(10)
norm.pdf(r)
norm.logpdf(r)                      # computational inexpensive to work with log pdf

norm.cdf(r)
norm.logcdf(r)