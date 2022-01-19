#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""



Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info -e
    !git branch -a

*********************************


"""
from typing import Tuple
import math

def normal_approximation_to_binomial(n: int,
                                     p: float) -> Tuple[float, float]:
    """returns mu and sigma corresponding to a Binomial(n,p)"""
    mu = n * p
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

from probability import normal_cdf

# The normal_cdf is the probability the variable is below a threshold
normal_probability_below = normal_cdf

# Its above the threshold if its not below
def normal_probability_above(lo: float,
                             mu: float = 0,
                             sigma: float = 1) -> float:
    """the probability that an N(mu, sigma) is greater than lo"""
    return 1 - normal_cdf(lo, mu, sigma)

# Its between if its less than hi but not less than lo
def normal_probability_between(lo: float, 
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """the probability that an N(mu, sigma) is between lo and high"""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# Its outside if its not between
def normal_probability_outside(lo: float, 
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """the probability that an N(mu, sigma) is between lo and high"""
    return 1 - normal_probability_between(lo, hi, mu, sigma)

from probability import inverse_normal_cdf

def normal_upper_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bound(probability: float,
                           mu: float =0,
                           sigma: float = 1) -> Tuple[float, float]:
    """
    Returns the symmetric (about the mean) bounds
    that contain the specified probability
    """
    tail_probability = ( 1 - probability ) / 2
    
    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    
    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    
    return lower_bound, upper_bound

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

assert mu_0 == 1000 * 0.5
assert sigma_0 == math.sqrt(1000 * 0.5 * (1 - 0.5))

"""
    We need to make a decision about significance,
    how willing are we to make a TYPE 1 error (false positive),
    in which we reject H0 (null hypothesis) even though it is true.
    let's keep it at 5%
    Read chapter 7, 8, 9 10 from David Spiegelhalter's The Art of Statistics
    to understand why this choice and how and when to change it.
    
    Now if 5% is the number of times when we are ok making an error,
    then 95% is # of times when we want to be confident
    that we didn't make the error.
    Hence, that's our probability of correctness/success
"""

lower_bound, upper_bound = normal_two_sided_bound(0.95, mu_0, sigma_0)

print(f"lower bound: {lower_bound}, upper bound: {upper_bound}")

"""
    Assuming P(HEAD) really equals 0.5 (i.e., H0 is true),
    there is just a 5% chance we observe an X that lies outside this interval,
    (lower_bound, upper_bound calculated above)
    which is the exact significance we wanted.
    
    Said differently, if H0 is true, then, 
    approximately 19 times out of 20, this test will give the correct result.
"""

"""
    We are also often interested in the power of a test, 
    which is the probability of not making a TYPE2 error (“false negative”), 
    in which we fail to reject H0 even though it’s false. 
    In order to measure this, we have to specify what exactly H0 being false means.
    (Knowing merely that P(HEAD) is not 0.5
     doesn’t give us a ton of information about the distribution of X.) 
    In particular, let’s check what happens if P(HEAD) is really 0.55,
    so that the coin is slightly biased toward heads.
    In that case, we can calculate the power of the test as below
"""

# 95% bounds based on assumption P(HEAD) is 0.5
lo, hi = normal_two_sided_bound(0.95, mu_0, sigma_0)

# actual mu, sigma based on P(HEAD) = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# a TYPE2 error means we fail to reject the null hypothesis, H0,
# which will happen when X is still in our original interval
type2_error_probability = normal_probability_between(lo, hi, mu_1, sigma_1)

power = 1 - type2_error_probability

print(power)

"""
    Imagine instead that our null hypothesis was that the coin 
    is not biased toward heads, or that P(HEAD) ≤ 0 . 5. 
    In that case we want a one-sided test that rejects the null hypothesis 
    when X is much larger than 500 but not when X is smaller than 500. 
    So, a 5% significance test involves using normal_probability_below 
    to find the cutoff below which 95% of the probability lies.
"""

hi = normal_upper_bound(0.95, mu_0, sigma_0)
print(hi)
# 526 ( < 531, since we need more probability in the upper tail)

type2_error_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type2_error_probability

print(power)

"""
    This is a more powerful test, 
    since it no longer rejects H0 when X is below 469 
    (which is very unlikely to happen if H1 is true) 
    and instead rejects H0 when X is between 526 and 531 
    (which is somewhat likely to happen if H1 is true).
"""

"""
    An alternative way of thinking about the preceding test involves p-values.
    Instead of choosing bounds based on some probability cutoff, 
    we compute the probability assuming H0 is true 
    that we would see a value at least as extreme as the one we actually observed.
"""

def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    How likely are we to see a value at least as extreme as x (in either
    direction) if our values are from a N(mu, sigma)?
    """
    if x >= mu:
        # x is greater than the mean, so the tail is everything greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # x is less than the mean, so the tail is everything less than x
        return 2 * normal_probability_below(x, mu, sigma)

# If we were to see 530 heads, we would compute
print( two_sided_p_value(529.5, mu_0, sigma_0) )        # 0.062

# let's check if this is a sensible estimate, by running a simulation
import random

extreme_value_count = 0
for _ in range(1000):
    num_heads = sum(1 if random.random() < 0.5 else 0    # Count # of heads
                    for _ in range(1000))                # in 1000 flips,
    if num_heads >= 530 or num_heads <= 470:             # and count how often
        extreme_value_count += 1                         # the # is 'extreme'

# p-value was 0.062 => ~62 extreme values in 1000 tries
assert 59 < extreme_value_count < 65 , f"{extreme_value_count}"
































