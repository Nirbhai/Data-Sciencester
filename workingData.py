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

from statss import mean

print(f" mean of uniform data set: {mean(uniform)}")
print(f" mean of normal data set: {mean(normal)}")

from statss import standard_deviation
print(f" std dev of uniform data set: {standard_deviation(uniform)}")
print(f" std dev of normal data set: {standard_deviation(normal)}")

"""
NOTE
-----------------------------------------------------------------------
Do not name your files same as any standard python lobrary names,
such as statistics.py
You will inadvertantly run into import errors,
if you try to import your local module.
In case you have to have to,
import it as directoryName.filename - haven't checked but it shall work
-----------------------------------------------------------------------
"""

plot_histogram(uniform, 10, "Uniform Histogram")

plot_histogram(normal, 10, "Normal Histogram")

import pandas as pd
import plotly.express as px

# below three lines helps choose where to render the plotly plots
# it needs plotly dependency kaleido installed for in-IDE rendering as svg
import plotly.io as pio
pio.renderers.default = 'svg'
#pio.renderers.default = 'browser'

df = pd.DataFrame(uniform)
fig = px.histogram(df, x=df[0], title="plotly Uniform Histogram")
fig.show()
print(df.describe())

df = pd.DataFrame(normal)
fig = px.histogram(df, x=df[0], title="plotly Normal Histogram")
fig.show()
print(df.describe())

def random_normal() -> float:
    """returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [ x + random_normal() / 2 for x in xs ]
ys2 = [ -x + random_normal() / 2 for x in xs ]

from plotly.subplots import make_subplots
import plotly.graph_objects as go

df1 = pd.DataFrame(ys1)
df2 = pd.DataFrame(ys2)

# plotting individual graphs

fig1 = px.histogram(df1, x = df1[0], title="Normal Distribution 1")
fig1.show()

fig2 = px.histogram(df2, x = df2[0], title="Normal Distribution 2")
fig2.show()

# plotting both graphs side by side
fig = make_subplots(
    rows = 1,
    cols = 2,
    subplot_titles = ("Distribution of ys1", "Distribution of ys2")
    )



fig.add_trace(
    (
        go.Histogram( x = df1[0], name = "ys1" )
    ),
    row = 1,
    col = 1
    )


fig.add_trace(
    (
        go.Histogram( x = df2[0], name = "ys2" )
    ),
    row = 1,
    col = 2
    )

fig.update_layout(
                    height=600,
                    width=1200,
                    title_text="Both datasets are normally distributed",
                    legend_orientation = "h"
                )
fig.show()
# both look similar 
# lets see their joint distribution with xs

plt.figure()
plt.scatter(
        xs, ys1,
        marker = '.',
        color = 'black',
        label = 'ys1'
    )

plt.scatter(
        xs, ys2,
        marker = '.',
        color = 'red',
        label = 'ys2'
    )

plt.xlabel("xs")
plt.ylabel("ys")
plt.legend(loc = 9)
plt.title("Very different joint distributions")
plt.show()

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter(x = xs, y = ys1, 
                         mode = "markers", name = "ys1")
              )
fig.add_trace(go.Scatter(x = xs, y = ys2, 
                         mode = "markers", name = "ys2"),
              secondary_y=True)
fig.update_layout(
                    title_text="Very different joint distributions",
                    legend_orientation = "h"
                )
fig.show()

# if plotly is used with dataframes of pandas
# it automatically adds x and y label from dataframe columns
# and probably other auto-things as well
# plotly is very well suited for working with pandas dataframes

from statss import correlation

print(correlation(xs, ys1))
print(correlation(xs, ys2))






























