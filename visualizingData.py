#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

I believe that visualization is one of the most powerful means of achieving goals.
    - Harvey Mackay


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



























