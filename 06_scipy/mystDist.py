from scipy.stats import skewnorm, truncnorm
from numpy.random import randn

def mysteryDistribution1(n):

    return(skewnorm.rvs(0.4, size=n))

def mysteryDistribution2(n):

    return(truncnorm.rvs(-2.6, 2.6, size=n))

def mysteryDistribution3(n):

    return(randn(n))

def mysteryDistribution4(n):

    return(randn(n))