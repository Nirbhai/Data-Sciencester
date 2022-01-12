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
multi_line_string = """first line
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

empty_dict1 = {}      # pythonic way
empty_dict2 = dict()  # also works, but not pythonic

grades = {"Randeep": 80, "Jasmeet": 95}

Randeep_grade = grades["Randeep"]
assert Randeep_grade == 80


try:
    Gurdas_grade = grades["Gurdas"]
except KeyError:
    print("no grade for Gurdas.")

# in method for dictionaries is very fast, as compared to lists
Randeep_has_grade = "Randeep" in grades
Gurdas_has_grade = "Gurdas" in grades

assert Randeep_has_grade == True
assert Gurdas_has_grade == False

"""
    Dictionaries have a get method that returns a default value 
    (instead of raising an exception) when you look up a key 
    that’s not in the dictionary
"""

Randeep_grade = grades.get("Randeep", 0)
Gurdas_grade = grades.get("Gurdas", 0)
koi_v_grade = grades.get("koi v")    # default value to be returned is None


assert Randeep_grade == 80
assert Gurdas_grade == 0
assert koi_v_grade == None

grades["Jasmeet"] = 90    # replaces old value with new one
grades["Gurdas"] = 88     # addes a new key value pair to the dict

num_students = len(grades)
assert num_students == 3

# dictionaries can be used to represent structured data
# though there are other better ways too
tweet = {
    "user" : "Randeep Singh",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()           # iterable for keys
tweet_values = tweet.values()       # iterable for values
tweet_items = tweet.items()         # iterable for (key, value) tuples

"""
Question -- ??
--------------
    What are iterables?
    how to iterate over them?
    can you store them in a variable?
    what type that variable will be?

ANSWER --
--------------

"""

"user" in tweet_keys                # works but non-pythonic
"user" in tweet                     # pythonic way of checking for keys

"Randeep Singh" in tweet_values     #slow but only way to check

"""
    Dictionary keys must be “hashable”; 
    in particular, you cannot use lists as keys. 
    If you need a multipart key, you should probably use a tuple 
    or figure out a way to turn the key into a string.
"""


document = ["data", "science", "from", "scratch"]

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

"""
    You could also use the “forgiveness is better than permission” approach 
    and just handle the exception from trying to look up a missing key
"""

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

# third approach is to use .get method
# as it behaves gracefully for missing keys
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

"""
    A defaultdict is like a regular dictionary, 
    except that when you try to look up a key it doesn’t contain, 
    it first adds a value for it 
    using a zero-argument function you provided when you created it. 
    In order to use defaultdicts, you have to import them from collections
"""

word_counts = defaultdict(int)      # int produces 0
for word in document:
    word_counts[word] += 1

# some more examples of using defaultdict

grades_dd_list = defaultdict(list)  # list produces an empty list
grades_dd_list["Randeep"].append(80)

assert grades_dd_list["Randeep"] == [80]
assert grades_dd_list["Randeep"][0] == 80

grades_dd_dict = defaultdict(dict)  # dict produces an empty dict
grades_dd_dict["Randeep"]["marks"] = 80
grades_dd_dict["Randeep"]["grade"] = "B+"

print(grades_dd_dict)
print(grades_dd_dict["Randeep"].keys())
assert  "marks" in grades_dd_dict["Randeep"].keys()
assert "grade" in grades_dd_dict["Randeep"].keys()

# you can also provide your won zero-argument functions as parameter to defaultdict
grades_dd_pair = defaultdict(lambda: [0, 0])
grades_dd_pair[1][1] = 3

print(grades_dd_pair)
assert grades_dd_pair[1][0] == 0
assert grades_dd_pair[1][1] == 3

name_city_state_dd = defaultdict(lambda: ["none", "none"])
name_city_state_dd["Shiv Kumar Batalvi"][0] = "Batala"
name_city_state_dd["Shiv Kumar Batalvi"][1] = "Punjab"

print(name_city_state_dd)
assert name_city_state_dd["Shiv Kumar Batalvi"] == ["Batala", "Punjab"]

# A Counter turns a sequence of values 
# into a defaultdict(int)-like object mapping keys to counts

c = Counter([0,2,1,1])
print(c)
assert c[1] == 2

# recall, document is a list of words
word_counts = Counter(document)

# Counter instance has a most_common method that is frequently useful
document.extend(["science", "science", "science", "data"])
word_counts = Counter(document)
for word, count in word_counts.most_common(2):
    print(word, count)
    assert word in ("data", "science")
    assert count in [2, 4]

# set is a collection of distinct elements. 
# A set can be defined by listing its elements between curly braces
primes_below_10 = {2, 3, 5, 7}

# as {} signifies an empty dictionary
# we can't use it to define an empty set
empty_set = set()
s = set()

s.add(1)
s.add(2)
s.add(2)

assert len(s) == 2
print (1 in s)
assert (1 in s) == True
assert (3 in s) == False

"""
    We’ll use sets for two main reasons. 
    The first is that "in" is a very fast operation on sets. 
    If we have a large collection of items 
    that we want to use for a membership test, 
    a set is more appropriate than a list
"""

hundreds_of_other_words = []

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

assert ("zip" in stopwords_list) == False
     # False, but have to check every element

stopwords_set = set(stopwords_list)
assert ("zip" in stopwords_set) == False
      # very fast to check

# 2nd use case is to find distinct items in a collection
item_list = [1, 2, 3, 1, 2, 3]
number_of_items = len(item_list)
item_set = set(item_list)
number_of_distinct_items = len(item_set)
distinct_item_list = list(item_set)

assert number_of_items == 6
assert number_of_distinct_items == 3
assert distinct_item_list == [1,2,3]

#ternary if-then-else one liner
parity = "even" if x%2 == 0 else "odd"

# range(x) goes from 0 to x-1
for x in range(10):
    print(f"{x} is less than 10")

for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)

one_is_less_than_two = 1 < 2
assert one_is_less_than_two == True

true_equals_false = True == False
assert true_equals_false == False

x = None
assert x == None        # non-pythonic way to check for None
assert x is None        # pythonic way to check for None

"""
    Python lets you use any value where it expects a Boolean. 
    The following are all “falsy”:
            False
            None
            []      (an empty list)
            {}      (an empty dictionary)
            set()   (an empty set)
            ""
            0
            0.0
    Pretty much anything else gets treated as "True". 
    This allows you to easily use if statements to test for 
    empty lists, empty strings, empty dictionaries, and so on. 
    It also sometimes causes tricky bugs 
    if you’re not expecting this behavior
"""

def some_function_that_returns_a_string():
    return ""

s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

# A shorter (but possibly more confusing) way of doing the same is:
first_char = s and s[0]
# since "and" returns its second value when the first is “truthy,” 
# and the first value when it’s not.

# check if x is a number or possibly None
x = "yo"
safe_x = x or 0
print(safe_x)

safe_x = x if x is not None else 0
print(safe_x)
# but x was a string, not a number
# so this is not a good check

"""
    Python has an "all" function, which takes an iterable 
    and returns "True" precisely when every element is truthy, 
    and an "any" function, which returns "true"
    when at least one element is truthy
"""

all1 = all([True, 1, {3}])      # True, all are truthy
all2 = all([True, 1 , {}])      # False, empty dict is falsy
any1 = any([True, 1 , {}])      # True, True is truthy
all3 = all([])                  # True, no falsy elements in the list
any2 = any([])                  # False, no truthy elements in the list

assert all1 is True
assert all2 is False
assert any1 is True
assert all3 is True
assert any2 is False


x = [4, 1, 3, 2]

y = sorted(x)
    # sorted() method returns a sorted list, original unchanged
    
assert x == [4, 1, 3, 2]
assert y == [1, 2, 3, 4]

x.sort()
    # .sort() method sorts "in-place"

assert x == [1, 2, 3, 4]

x = [-4, 1, 3, -2]

# sort the list by absolute value from largest to smallest
y = sorted(x, key=abs, reverse=True)

assert y == [-4, 3, -2, 1]
assert x == [-4, 1, 3, -2]

x.sort(key=abs, reverse=True)

assert x == [-4, 3, -2, 1]

# instead of comparing the elements themselves, 
# you can compare the results of a function that you specify with key
# remember the word_counts
# sort the words & counts from highest count to lowest
wc = sorted(word_counts.items(),
            key=lambda item: item[1] ,
            reverse=True)
print(wc)

"""
    Frequently, you’ll want to transform a list into another list 
    by choosing only certain elements, 
    or by transforming elements, or both. 
    The Pythonic way to do this is with list comprehensions
"""

even_numbers = [x for x in range(7) if x%2 == 0]
assert even_numbers == [0, 2, 4, 6]

squares = [x*x for x in range(7)]
assert squares == [0, 1, 4, 9, 16, 25, 36]

even_squares = [x*x for x in even_numbers]
assert even_squares == [0, 4, 16, 36]

square_dict = {x: x*x for x in range(7)}
assert square_dict[3] == 9
print(square_dict)

square_set = {x*x for x in (-1, 0, 1)}
assert len(square_set) == 2
print(square_set)

zeros = [0 for _ in even_numbers]
assert len(zeros) == len(even_numbers)

pairs = [(x,y)
         for x in (0,1,2)
         for y in range(3)]
print(pairs)

"""
Question -- ??
--------------
    What is the difference between lambda functions and list comprehensions?
    Which one to use where?

ANSWER --
--------------

"""
increasing_pairs = [(x,y)
                    for x in range(3)
                    for y in range(x+1,3)]
print(increasing_pairs)

























