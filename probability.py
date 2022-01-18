#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

For a data scientist it is beneficial to think of Probability 
as a way of quantifying the uncertainty associated with events 
chosen from some universe of events.
Rather than getting technical about what these terms mean, 
think of rolling a die. The universe consists of all possible outcomes. 
And any subset of these outcomes is an event; 
for example, “the die rolls a 1” or “the die rolls an even number.”
    - Joel Grus


Notationally, we write P(E) to mean “the probability of the event E”

Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info -e
    !git branch -a

*********************************


"""

"""
    Roughly speaking, we say that two events E and F are dependent 
    if knowing something about whether E happens 
    gives us information about whether F happens (and vice versa). 
    Otherwise, they are independent.
    For instance, if we flip a fair coin twice, 
    knowing whether the first flip is heads 
    gives us no information about whether the second flip is heads. 
    These events are independent. 
    On the other hand, knowing whether the first flip is heads
    certainly gives us information about whether both flips are tails.
    These two are dependent events.
"""

import enum, random

# an Enum is a typed set of enumerated values. 
# We can use them to make our code more descriptive and readable.

class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])


both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    
    if older == Kid.GIRL:
        older_girl += 1
    if older == Kid.GIRL and younger == Kid.GIRL:
        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girl += 1

print("P(both | older):", both_girls / older_girl)
print("P(both | either):", both_girls / either_girl)

x = ( .99 * .0001 ) / ( ( .99 * .0001 ) + ( .01 * .9999 ) )
print(x)

# probability density function for uniform distribution
def uniform_pdf(x: float) -> float:
    return 1 if 0 <= x < 1 else 0

# cummulative distribution function for uniform distribution
def uniform_cdf(x: float) -> float:
    """Returns the probability that a uniform random variable is <= x"""
    if x < 0.0: return 0      # uniform random is never less than 0
    elif x < 1.0: return x    # e.g. P( X <= .4 ) = 0.4
    else: return 1          # uniform random is always less than 1

import matplotlib.pyplot as plt

x = [ x / 10.0 for x in range(-10, 20)]
y = [uniform_pdf(x_i) for x_i in x]

plt.plot(x, y)
plt.title("The Uniform PDF")
plt.show()


#y = uniform_cdf(x)
y = [uniform_cdf(x_i) for x_i in x]
#print(x)

plt.plot(x, y)
plt.title("The Uniform CDF")
plt.show()

# probability distribution function for normal distribution
import math

# whwn mu = 0 and sigma = 1, it's called the "standard" normal distribution
def normal_pdf(x: float, 
              mu: float = 0,
              sigma: float = 1) -> float:
    return ( math.exp( - (( x - mu) ** 2) 
                      / ( 2 * (sigma ** 2) ) )
            / ( math.sqrt( 2 * math.pi) * sigma )
            )

x = [x_i / 10.0 for x_i in range(-50, 50)]
y1 = [normal_pdf(x_i, sigma=1) for x_i in x]
y2 = [normal_pdf(x_i, sigma=2) for x_i in x]
y3 = [normal_pdf(x_i, sigma=0.5) for x_i in x]
y4 = [normal_pdf(x_i, mu=1) for x_i in x]

plt.plot(x, y1, '-', label='mu=0, sigma=1')
plt.plot(x, y2, '--', label='mu=0, sigma=2')
plt.plot(x, y3, ':', label='mu=0, sigma=0.5')
plt.plot(x, y4, '-.', label='mu=1, sigma=1')
plt.legend()
plt.title("Various normal PDFs")
plt.show()

### -------------START----------------
### Concepts to revist. Not clear yet.
### ----------------------------------

def normal_cdf(x: float,
               mu: float = 0,
               sigma: float = 1) -> float:
    return (1 + math.erf( (x - mu) / ( math.sqrt(2) * sigma) )) / 2

y1 = [normal_cdf(x_i, sigma=1) for x_i in x]
y2 = [normal_cdf(x_i, sigma=2) for x_i in x]
y3 = [normal_cdf(x_i, sigma=0.5) for x_i in x]
y4 = [normal_cdf(x_i, mu=1) for x_i in x]

plt.plot(x, y1, '-', label='mu=0, sigma=1')
plt.plot(x, y2, '--', label='mu=0, sigma=2')
plt.plot(x, y3, ':', label='mu=0, sigma=0.5')
plt.plot(x, y4, '-.', label='mu=1, sigma=1')
plt.legend(loc=4)   # bottom right
plt.title("Various normal CDFs")
plt.show()

def inverse_normal_cdf(p: float,
                       mu: float = 0,
                       sigma: float = 1,
                       tolerance: float = 0.00001) -> float:
    """Find approximate inverse using Binary Search"""
    
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z = -10.0                      # normal_cdf(-10) is (very close to) 0
    hi_z  =  10.0                      # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2     # Consider the midpoint
        mid_p = normal_cdf(mid_z)      # and the cdf's value there
        if mid_p < p:
            low_z = mid_z              # Midpoint too low, search above it
        else:
            hi_z = mid_z               # Midpoint too high, search below it
    
    return mid_z

### --------------END-----------------
### Concepts to revist. Not clear yet.
### ----------------------------------

def bernoulli_trial(p: float) -> int:
    """returns 1 with probability p and 0 with probability 1 - p"""
    return 1 if random.random() < p else 0

def binomial(n: int, p: float) -> int:
    """Returns the sum of n bernoulli(p) trials"""
    return sum( bernoulli_trial(p) for _ in range(n) )

# plotting a binomial

from collections import Counter

def binomial_histogram(p: float,
                       n: int,
                       num_points: int) -> None:
    """Picks points from a Binomial(n,p) and plots their histogram"""
    
    data = [binomial(n,p) for _ in range(num_points)]
    
    # a Bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color = '0.75')
    
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    
    # A line chart to show the normal distribution
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs. Normal approximation")
    plt.show()

binomial_histogram(0.75, 100, 10000)


"""
    scipy.stats:
        contains PDF and CDF functions 
        for most of the popular probability distributions.
"""





































