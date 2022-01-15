#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

I believe that visualization is one of the most powerful means of achieving goals.
    - Harvey Mackay

matplotlib is good for basic dataviz
but checkout:
    seaborn
    altair-viz
    d3
    bokeh

Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info -e
    !git branch -a

*********************************


"""

from matplotlib import pyplot as plt

years = [1950, 1960, 1970,
         1980, 1990, 2000,
         2010]
gdp = [300.2, 543.3, 1075.9,
       2862.5, 5979.6, 10289.7,
       14958.3]

# create a line chart, years on x-axis, gdp on y.axis
plt.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')

# add a title
plt.title("Nominal GDP")

# add a lable to the y-axis
plt.ylabel("Billions of $")
plt.show()

# Bar chart is a good choice when you want to show 
# how some quantity varies amongst a discrete set of items.

movies = ["Annie Hall", "Ben-Hur", "Casablanca",
          "Gandhi", "West Side Story"]

num_oscars = [5, 11, 3, 8, 10]

# plot bars with left x-coordinates [0,1,2..], heights with num_oscars
plt.bar(range(len(movies)), num_oscars)


plt. title("My Favourite Movies")       # add a title
plt.ylabel("# of Academy Awards")       # label the y-axis

# label the x-axis with movie names at bar centers
plt.xticks(range(len(movies)), movies)

plt.show()

# Bar chart can also be a good choice for plotting
# histograms of bucketed numeric values

from collections import Counter
grades = [ 83, 95, 91, 87,
           70, 0, 85, 82,
           100, 67, 73, 77,
           0]

# Bucketing the grades by decile
# putting 100 in the 90s bucket
histogram = Counter(min(grade//10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],  # shift bars by 5
        histogram.values(),                 # give each bar its correct height
        9,                                 # give each bar a width of 10
        edgecolor = (0, 0, 0))              # black edges for each bar

plt.axis( [-5, 105,                         # y-axis from -5 to 105
           0, 5])                           # x-axis from 0 to 5

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of students")
plt.title("Distribution of exam 1 grades")
plt.show()


# an example of a misleading chart

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'Machine Learning'")

# misleading y-axis only shows the part above 500
plt.axis([2016.5, 2018.5, 
          499, 506])

plt.title("Look at the 'Huge' increase.")
plt.show()



plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'Machine Learning'")

# non-misleading y-axis but also uninteresting
plt.axis([2016.5, 2018.5, 
          0, 550])

plt.title("Not so huge anymore.")
plt.show()


# Line charts are good for showing trends

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# we can make multiple calls to plt.plot
# to chow multiple series on the same chart
plt.plot(xs, variance,      'g-',   label = "variance")     # green solid line
plt.plot(xs, bias_squared,  'r-.',  label = "bias^2")       # red dot-dashed line
plt.plot(xs, total_error,   'b:',   label = "total_error")  # blue dotted line

# because we have assigned labels to each series
# we can get a legend for free (loc=9 means "top center")
plt.legend(loc = 9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The BIas-Variance tradeoff")
plt.show()


# Scatterplot is a good choice for visualizing the relationship
#  between two paired sets of data

friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
        xy=(friend_count, minute_count), # Put the label with its point
        xytext=(5, -5),                  # but slightly offset
        textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()


test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.show()

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Are Comparable")
plt.axis("equal")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.show()























