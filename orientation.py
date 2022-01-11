#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Today is 2nd day as Head of data science at Data Sciencester.
It's the orientation day.


Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info -e
    !git branch -a

*********************************


"""


# The pound sign marks the start of a comment. Python itself
# ignores the comments, but they're helpful for later when you're 
# revisiting your code or someone else.

for i in [1,2,3]:
    print(i)                 # comments can be inserted like this as well
    for j in ["a", "b", "c"]:
        print(j)
print("done looping")

# Whitespace is ignored inside parentheses and brackets

lists_of_lists = [[1,2,3] , [4,5,6] , [7,8,9]]

easier_to_read_list_of_lists = [[1,2,3],
                                [4,5,6],
                                [7,8,9]]

"""
    Question -- ??
    --------------
    Does Import module
        and
    from module import *
    mean the same?
"""

# Pythonic way is to just import the particular function
# you need from a module instead of importing all 
# the contents of a module into your namespace

# If you were a bad person, 
# you could import the entire contents of a module into your namespace
# However, since you are not a bad person, you won’t ever do this.

from collections import defaultdict, Counter

# You can rename the function that you are importing
# to make it easier for you to use/call it again and again

import matplotlib.pyplot as plt


""" 
    Python functions are first-class, 
    which means that we can assign them to variables 
    and pass them into functions just like any other arguments:
"""

def doubling(x):
    """
    this function multiplies it's input by 2
    """
    return x * 2

def apply_to_one(foo):
    """
    calls the function foo with 1 as its argument
    """
    return foo(1)

my_double = doubling      # refers to the previously defined function doubling

x = apply_to_one(my_double)

assert x == 2

y = apply_to_one(lambda x: x + 4)

assert y == 5

# Don't use lambdas to assign to variables
another_doubling = lambda x: 2 * x    # y u do dis

def another_doubling(x):
    """
    Do this instead
    """
    return 2 * x

# Function parameters can also have default arguments
# Function arguments can also have default values
def my_print(msg = "default message"):
    print(msg)

my_print("Yo !!")
my_print()

# It is sometimes useful to specify arguments by name
def full_name(first = "what's-his-name", last = "Something"):
    return first + " " + last

print(full_name("Randeep", "Singh"))
print(full_name("Randeep"))
print(full_name(last="Singh"))

single_quoted_string = 'chakk'
double_quoted_string = "CHAKK"
#both are fine, as long as the quotes match

# Python uses backslashes to encode special characters
tab_string = "\t"
assert len(tab_string) == 1

# If you want backslashes as backslashes
# create raw strings
not_tab_string = r"\t"
assert len(not_tab_string) == 2

# Multiline strings using three double quotes
multi_line_string = """ first line
2nd line
3rd line"""

first_name = "Randeep"
last_name = "Singh"

# string addition way
full_name1 = first_name + " " + last_name

# string.format way
full_name2 = "{0} {1}".format(first_name, last_name)

# f-string way
full_name3 = f"{first_name} {last_name}"

assert full_name1 == full_name2
assert full_name2 == full_name3

try:
    print(0 / 0)
except ZeroDivisionError:
    print("Division by zero not allowed")

# List is an ordered collection

integer_list = [1, 2 ,3]
hetrogeneous_list = [1, "yo", 0.1, True]
list_of_list = [integer_list, hetrogeneous_list, []]

list_length = len(integer_list)
assert list_length == 3

list_sum = sum(integer_list)
assert list_sum == 6

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# lists are indexed from zero
zero = x[0]
assert zero == 0

one = x[1]
assert one ==1

nine = x[-1]  # pythonic for last element
assert nine == 9

eight = x[-2]  # pythonic for 2nd-last element
assert eight == 8

# getting and setting can both be done by indexing
x[0] = 10
assert x == [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]


"""
    You can also use square brackets to slice lists. 
    The slice means all elements from (inclusive) to (not inclusive). 
    If you leave off the start of the slice, 
    you’ll slice from the beginning of the list, 
    and if you leave of the end of the slice, 
    you’ll slice until the end of the list
"""

first_three = x[:3]
assert first_three == [10, 1, 2]

three_to_end = x[3:]
assert three_to_end == [3, 4, 5, 6, 7, 8, 9]

one_to_four = x[1:5]
assert one_to_four == [1, 2, 3, 4]

last_three = x[-3:]
assert last_three == [7, 8, 9]

without_first_and_last = x[1:-1]
assert without_first_and_last == [1, 2, 3, 4, 5, 6, 7, 8]

copy_of_x = x[:]
assert copy_of_x == [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]


"""
    Question -- ??
    --------------
    x = [1, 2, 3]
    way1 = x[:]
    way2 = x
    
    What is the difference between way1 and way2 ?
    
    ANSWER --
    --------------
    way1 will create a separate copy of x and store it in variable way1.
    way2 will just create a reference to x and whenever x changes,
    way2 will be changed and whenever way2 is changed,
    x will also correspondingly change.
"""

# Slicing can be used on other sequential types as well
# such as strings

# slicing can take a third argument as well, called stride (step)
# stride(step) can be negative as well

every_third = x[::3]
assert every_third == [10, 3, 6, 9]

five_to_three = x[5:2:-1]
assert five_to_three == [5, 4, 3]

# check list membership by using in operator
assert 2 in x
print(2 in x)
print(0 in x)
print(x)
# in operator takes O(n) time to check for membership
# use catiously

x = [1, 2, 3]
# list.extend will modify the list in place
x.extend([4, 5, 6])
assert x == [1, 2, 3, 4, 5, 6]

x = [1, 2, 3]
# list addition will not modify the original list
y = x + [4, 5, 6]

assert x == [1, 2, 3]
assert y == [1, 2, 3, 4, 5, 6]

# list.append will add one element at the end of list
x.append(4)
assert x == [1, 2, 3, 4]
assert x[-1] == 4
assert len(x) == 4

# unpacking a list
_, y = [1, 2]
assert _ == 1    # underscore as variable name is used for throw-away data
assert y == 2

"""
    Tuples are lists’ immutable cousins. 
    Pretty much anything you can do to a list 
    that doesn’t involve modifying it, you can do to a tuple. Y
    ou specify a tuple by using parentheses (or nothing) i
    nstead of square brackets
"""

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4

my_list[1] = 3
assert my_list == [1, 3]

try:
    my_tuple[1] = 4
except TypeError:
    print("Can not modify a tuple")

# tuples are a convenient way to return multiple values from a function
def sum_product(x, y):
    return (x+y), (x*y)

sp = sum_product(1, 2)
assert sp == (3, 2)
# here sp == 3, 2 without parenthesis will not work
# it only works while defining a tuple

s, p = sum_product(1, 2)
assert s == 3
assert p == 2

# tuples and lists can be used for multiple assignment
x, y = 1, 2
assert x == 1
assert y == 2

x, y = [3, 4]
assert x == 3
assert y == 4

# pythonic way of swapping values
x, y = y, x
assert x == 4
assert y == 3



































