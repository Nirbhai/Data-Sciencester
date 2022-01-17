#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

The numbers have no way of speaking for themselves.
We speak for them.
We imbue them with meaning.
    Nate Silver, The Signal and the Noise


Data exploration = Statistics
and Data exploration is the first or second thing 
that you should always do 
when you get a dataset.
    - me

Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info -e
    !git branch -a

*********************************


"""
from collections import Counter
import matplotlib.pyplot as plt
# num_friends[i] = number of friends i-th Data-Sciencester user has
num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

friend_counts = Counter(num_friends)
print (friend_counts)

xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101,
          0, 25])
plt.title("Histogram of friend counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

num_points = len(num_friends)

assert num_points == 204

largest_value = max(num_friends)
smallest_value = min(num_friends)

assert largest_value == 100
assert smallest_value == 1

sorted_values = sorted(num_friends)
assert smallest_value == sorted_values[0]
assert largest_value == sorted_values[-1]

### Central Tendencies ###

from typing import List

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

print(mean(num_friends))

# The underscores indicate that these are "private" functions, as they're
# intended to be called by our median function but not by other people
# using our statistics library.

def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[ len(xs) //2 ]

def _median_even(xs: List[float]) -> float:
    """if len(xs) is even, the median is mean of middle two elements"""
    xs_sorted = sorted(xs)
    mid_point = len(xs) // 2
    return (xs_sorted[mid_point - 1] + xs_sorted[mid_point]) / 2

def median(v: List[float]) -> float:
    """finds middle-most element/value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9 , 5]) == 5
assert median([1, 9, 2, 10]) == (2+9) / 2

print(median(num_friends))

def quantile(xs: List[float], p: float) -> float:
    """returns the p-th percentile element/value in xs"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

assert quantile(num_friends, 0.10) == 1
assert quantile(num_friends, 0.25) == 3
assert quantile(num_friends, 0.50) == median(num_friends)
assert quantile(num_friends, 0.75) == 9
assert quantile(num_friends, 0.90) == 13

def mode(xs: List[float]) -> List[float]:
    """returns a list, since there might be more than one mode"""
    counts = Counter(xs)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

assert set(mode(num_friends)) == {1, 6}
print(mode(num_friends))

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

assert data_range(num_friends) == 99

#from Data-Sciencester.linearAlgebra import sum_of_squares
#import linearAlgebra.sum_of_squares

from linearAlgebra import sum_of_squares

def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean, so the result has mean 0"""
    mean_element = mean(xs)
    return [x - mean_element for x in xs]

def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from mean"""
    assert len(xs) >=2, "variance requires at least 2 elements"
    
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (len(xs) - 1)

assert 81.54 < variance(num_friends) < 81.55

import math

def standard_deviation(xs: List[float]) -> float:
    """standard deviation is the square root of variance"""
    return math.sqrt(variance(xs))

assert 9.02 < standard_deviation(num_friends) < 9.04

def interquartile_range(xs: List[float]) -> float:
    """returns the difference between 75%-ile and 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)

assert interquartile_range(num_friends) == 6

# daily_minutes shows how many minutes per day each user spends on Data Sciencester
# and its order of elements corresponds to order of elements of num_friends
daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

assert len(daily_minutes) == len(num_friends)

daily_hours = [dm / 60 for dm in daily_minutes]

# Variance measures how a single variable deviates from its mean
# Covariance measures how two variables vary in tandem from their means

from linearAlgebra import dot

def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

assert 22.42 < covariance(num_friends, daily_minutes) < 22.43
assert 22.42 / 60 < covariance(num_friends, daily_hours) < 22.43 / 60

"""
    function-Dot (as implemented in linearAlgebra) 
    sums up the products of corresponding pairs of elements. 
    When corresponding elements of x and y are either both above their means 
    or both below their means, a positive number enters the sum. 
    When one is above its mean and the other below, 
    a negative number enters the sum. 
    Accordingly, a “large” positive covariance means 
    that x tends to be large when y is large and small when y is small. 
    A “large” negative covariance means the opposite, 
    that x tends to be small when y is large and vice versa. 
    A covariance close to zero means that no such relationship exists.
    
    Nonetheless, this number can be hard to interpret, for a couple of reasons:
        1. Its units are the product of the inputs’ units 
        (e.g., friend-minutes-per-day in the above example), 
        which can be hard to make sense of. (What’s a “friend-minute-per-day”?)
        
        2. If each user had twice as many friends (but the same number of minutes),
        the covariance would be twice as large. 
        But in a sense, the variables would be just as interrelated. 
        Said differently, it’s hard to say what counts as a “large” covariance.
    
    For this reason, it’s more common to look at the correlation, 
    which divides out the standard deviations of both variables.
    
    The correlation is unitless and always lies between 
    –1 (perfect anticorrelation) and 1 (perfect correlation). 
    A number like 0.25 represents a relatively weak positive correlation.
"""

def correlation(xs: List[float], ys: List[float]) -> float:
    """measures how much xs & ys vary in tandem about their means"""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x /stdev_y
    else:
        return 0        # if no variation, correlation is zero

assert 0.24 < correlation(num_friends, daily_minutes) < 0.25
assert 0.24 < correlation(num_friends, daily_hours) < 0.25

# lets examine the data

plt.scatter(num_friends, daily_minutes)
plt.title("Daily Minutes vs. # of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()

# The person with 100 friends (who spends only 1 minute per day on the site) 
# is a huge outlier, and correlation can be very sensitive to outliers. 
# What happens if we ignore him?

outlier = num_friends.index(100)    # index of outlier
num_friends_good = [x
                    for x in num_friends
                    if x != 100]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

daily_hours_good = [dmg / 60 for dmg in daily_minutes_good]

plt.scatter(num_friends_good, daily_minutes_good)
plt.title("Daily Minutes vs. # of friends - outlier")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()

# OBSERVATION: without the outlier in picture, the correlation is much stronger

assert 0.57 < correlation(num_friends_good, daily_minutes_good) < 0.58
assert 0.57 < correlation(num_friends_good, daily_hours_good) < 0.58

"""

Confounding Variables:
----------------------
    When an apparent association between two outcomes might be explained
    by some observed common factor that influences both,
    this common cause is called, a confounder or a confounding variable.
    
    A variable which is associated with both a response and a predictor,
    and which may explain some of their apparent relationship.
    Example:
        height and weight of children are strongly correlated,
        but much of this association is explained by 
        the age of the child.
        Here, age of the child is a confounding variable.

Simpson's Paradox:
------------------
    One not uncommon surprise when analyzing data is Simpson’s paradox,
    in which correlations can be misleading,
    when confounding variables are ignored.
    Carrying on with the above example of Data-Sciencester community,
    imagine that we can identify all out members as either 
    northern data scientists
    or
    southern data scientists,
    and decide to examine which group is friendlier.
    
    Region      # of members    Avg. # of friends
    North       101             8.2
    South       103             6.5
    
    It looks like Northeners are friendlier than the Southerners.
    
    But while playing with the data, you discover something very strange.
    If you look only at people with PhDs,
    the southerners have more friends on average.
    If you look only at people without PhDs,
    again the southerners have more friends on average.
    But how can that be ??
    
    Region  Degree      # of members    Avg. # of friends
    North   PhD         35              3.1
    South   PhD         70              3.2
    North   Non-PhD     66              10.9
    South   Non-PhD     33              13.4
    
    Once you account for the users’ degrees, 
    the correlation goes in the opposite direction! 
    Bucketing the data as North/South disguised the fact 
    that the East Coast data scientists skew much more heavily toward PhD types.
    
    This phenomenon crops up in the real world with some regularity. 
    The key issue is that correlation is measuring the relationship 
    between your two variables all else being equal. 
    If your dataclasses are assigned at random, 
    as they might be in a well-designed experiment, 
    “all else being equal” might not be a terrible assumption. 
    But when there is a deeper pattern to class assignments, 
    “all else being equal” can be an awful assumption.
    The only real way to avoid this is by knowing your data and 
    by doing what you can to make sure you’ve checked for 
    possible confounding factors. Obviously, this is not always possible. 
    If you didn’t have data on the educational attainment of 
    these 200 data scientists, you might simply conclude that 
    there was something inherently more sociable about the Northeners.


Correlation Caveats:
--------------------
    A correlation of zero indicates that there is no linear relationship 
    between the two variables. 
    However, there may be other sorts of relationships. 
    For example, if:
        x = [ -2, -1, 0, 1, 2]
        y = [  2,  1, 0, 1, 2]
        
        then x and y have zero correlation. 
        But they certainly have a relationship, each element of y equals 
        the absolute value of the corresponding element of x. 
        What they don’t have is a relationship in which 
        knowing how x_i compares to mean(x) gives us information about 
        how y_i compares to mean(y). 
        That is the sort of relationship that correlation looks for.
    
    In addition, correlation tells you nothing 
    about how large the relationship is.
        x = [ -2, -1, 0, 1, 2]
        y = [99.98, 99.99, 100, 100.01, 100.02]
        
        The above variables are perfectly correlated, 
        but depending on what you're measuring,
        it's quite possible that this relationship 
        isn't all that interesting or useful to you.


Correlation & Causation:
------------------------
    Correlation is not Causation
    if x and y are strongly correlated, that might mean 
        that x causes y, 
        that y causes x, 
        that each causes the other, 
        that some third factor causes both, 
        or nothing at all.
    
    Consider the relationship between num_friends and daily_minutes. 
    It’s possible that having more friends on the site causes 
    DataSciencester users to spend more time on the site. 
    This might be the case if each friend posts 
    a certain amount of content each day, 
    which means that the more friends you have, 
    the more time it takes to stay cur‐ rent with their updates.
    
    However, it’s also possible that the more time users spend 
    arguing in the DataSciencester forums, 
    the more they encounter and befriend like-minded people. 
    That is, spending more time on the site causes users to have more friends.
    
    A third possibility is that the users who are 
    most passionate about data science spend more time on the site 
    (because they find it more interesting) and 
    more actively collect data science friends 
    (because they don’t want to associate with anyone else).
    
    One way to feel more confident about causality is 
    by conducting randomized trials.
    
    For example:
        you could randomly choose a subset of your users 
        and show them content from only a fraction of their friends. 
        If this subset subsequently spent less time on the site, 
        this would give you some confidence that having more friends 
        causes more time to be spent on the site.

"""

x = [ -2, -1, 0, 1, 2]
y = [  2,  1, 0, 1, 2]
print(correlation(x, y))

x = [ -2, -1, 0, 1, 2]
y = [99.98, 99.99, 100, 100.01, 100.02]
print(correlation(x, y))


"""
    Some important statistics libraries:
            1. SciPy            ( https://scipy.org/ )
            2. Pandas           ( https://pandas.pydata.org/ )
            3. StatsModels      ( https://www.statsmodels.org/stable/index.html )
    
    3 books online statistics books suggested by Joel Grus:
        1. https://open.umn.edu/opentextbooks/textbooks/introductory-statistics
        2. https://onlinestatbook.com/
        3. https://openstax.org/details/introductory-statistics
"""










