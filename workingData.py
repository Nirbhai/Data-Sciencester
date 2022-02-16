#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Experts often possess more data than judgement.
    - Colin Powell

Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info -e
    !git branch -a

*********************************


"""

from typing import List, Dict
from collections import Counter
import math
import matplotlib.pyplot as plt

def bucketize(point: float, bucket_size: float) -> float:
    """Floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points: List[float],
                   bucket_size: float) -> Dict[float, int]:
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points: List[float],
                   bucket_size: float,
                   title: str = "") -> None:
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)

import random
from probability import inverse_normal_cdf

random.seed(0)

# uniform between -100 and 100
uniform = [200 * random.random() - 100 for _ in range(10000)]

# normal distribution with mean = 0, std dev = 57
normal = [57 * inverse_normal_cdf(random.random())
          for _ in range(10000)]

from statistics import mean

print(f" mean of uniform data set: {mean(uniform)}")
print(f" mean of normal data set: {mean(normal)}")

from statistics import standard_deviation









































