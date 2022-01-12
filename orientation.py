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
    
    ANSWER --
    --------------
    
"""

# Pythonic way is to just import the particular values
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


# assert False == True, "truthy no equals falsy"
assert True == 1, "truthiness in python is not to be taken lightly"

# one good debug practice is to assert function return values 
# to see if nothing is lost in calling and returning

def min_value(x):
    return min(x)

assert min_value([-1,-2,0,.9]) == -2, "min_value function misbehave"

# Another less common use is to assert things about inputs to functions
def smallest_item(x):
    assert x, "empty list has no smallest item"
    return min(x)

class CountingCLicker:
    """
        Here we’ll construct a class representing a “counting clicker,” 
        the sort that is used at the door to track how many people 
        have shown up for the “Data science in Bir” meetup.
        
        It maintains a count, 
        can be clicked to increment the count, 
        allows you to read_count, 
        and can be reset back to zero.
        
        To define a class, you use the keyword class and a PascalCase name.
        
        A class contains zero or more member functions. 
        By convention, each takes a first parameter, self, 
        that refers to the particular class instance.
        
        Normally, a class has a constructor, named __init__.
        It takes whatever parameters you need 
        to construct an instance of your class 
        and does whatever setup you need
    """
    def __init__(self, count = 0):
        self.count = count
    
    """
        Notice that the __init__ method name 
        starts and ends with double underscores. T
        hese “magic” methods are sometimes called “dunder” methods 
        (double-UNDERscore, get it?) and represent “special” behaviors.
        
        Class methods whose names start with an underscore 
        are—by convention—considered “private,” 
        and users of the class are not supposed to directly call them. 
        However, Python will not stop users from calling them.
        
        Another such method is __repr__, 
        which produces the string representation of a class instance.
    """
    
    def __repr__(self):
        return f"CountingClicker(count={self.count})"
    
    # public APIs of our class
    
    def click(self, num_times = 1):
        """ Click the clicker some number of times."""
        self.count += num_times
    
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0


# Although the constructor has a funny name, 
# we construct instances of the clicker using just the class name

clicker1 = CountingCLicker()                # initilaized to 0
clicker2 = CountingCLicker(100)             # initialized to 100
clicker3 = CountingCLicker(count = 100)   # explicit way of doing the same

assert clicker1.read() == 0, "clicker should start with count=0, but it isn't so"
assert clicker2.read() == clicker3.read(), "both clickers have been initialized to 100"

clicker1.click()
clicker1.click()
clicker1.click()

assert clicker1.read() == 3, "after 3 clicks, clicker count should be 3"

clicker1.click(10)

assert clicker1.read() == 13, "after 13 clicks, clicker count should be 3"

clicker1.reset()

assert clicker1.read() == 0, "after reset, clicker count should be 0"

"""
    We can create subclasses that inherit 
    some of their functionality from a parent class. 
    For example, we could create a non-reset-able clicker
    by using CountingClicker as the base class 
    and overriding the reset method to do nothing:
"""

# a subclass inherits all the behavior of its parent class
class NoResetClicker(CountingCLicker):
    # this class has all the methods of CountingCLicker
    # except that it has a reset method that does nothing
    
    def reset(self):
        pass
    
    """
        Question -- ??
        --------------
            Are "pass" and "continue" same?
            If not, what is the difference?

        ANSWER --
        --------------
    """

clicker4 = NoResetClicker()
assert clicker4.read() == 0
clicker4.click()
assert clicker4.read() == 1
clicker4.reset()
assert clicker4.read() == 1, "reset shouldn't do anything"

"""
    One nice thing about a list is that you can retrieve 
    specific elements by their indices. 
    But you don’t always need this! 
    A list of a billion numbers takes up a lot of memory. 
    If you only want the elements one at a time, t
    here’s no good reason to keep them all around. 
    If you only end up needing the first several elements, g
    enerating the entire billion is hugely wasteful.
    Often all we need is to iterate over the collection using "for" and "in". 
    In this case we can create generators, 
    which can be iterated over just like lists 
    but generate their values lazily on demand.
    
    One way to create generators is with functions and the yield operator
"""

def generate_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in generate_range(5):
    print(f"i: {i}")

# in fact, "range" is itself lazy

# we can even generate an infinite sequence with a generator 
# without running into memory issues.
# Be very careful while using such a generator.

def natural_numbers():
    """returns natural numbers, 1, 2, 3..
        one at a time.
        Be very careful while calling this function.
        Always call with a "break" logic in place.
    """
    i = 1
    while True:
        yield i
        i += 1

"""
    The flip side of laziness is that 
    you can only iterate through a generator once. 
    If you need to iterate through something multiple times, 
    you’ll need to either re-create the generator each time or use a list. 
    If generating the values is expensive, 
    that might be a good reason to use a list instead.
"""

# A second way to create generators 
# is by using "for" comprehensions wrapped in parentheses
evens_below_10 = (i for i in generate_range(10) if i % 2 == 0)
# Such a “generator comprehension” doesn’t do any work 
# until you iterate over it (using "for" or "next"). 
# We can use this to build up elaborate data- processing pipelines.

# None of the below computations *does* anything
# until we iterate over them
data = natural_numbers()
evens = (i for i in data if i % 2 == 0)
evens_squared = (i*i for i in evens)
evens_squared_ending_6 = (i for i in evens_squared if i % 10 == 6)

print(data)
print(evens_squared_ending_6)

"""
    Not infrequently, when we’re iterating over a list or a generator 
    we’ll want not just the values but also their indices. 
    For this common case Python provides an "enumerate" function, 
    which turns values into pairs - (index, value)
"""

names = ["Randeep", "Gurdas", "Jasmeet"]

# non-pythonic way
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# also non-pythonic way of doing same
_ = 0
for name in names:
    print(f"name {_} is {names[_]}")
    _ += 1

# pythonic way of doing same
for i, name in enumerate(names):
    print(f"name {i} is {names[i]}")

# using "enumerate" with generators
for i, j in enumerate(generate_range(5)):
    print(f"{i}: {j}")

import random as rand

rand.seed(10)
four_uniform_rands = [rand.random() for _ in range(4)]
print(four_uniform_rands)

"""
    The "random" module actually produces pseudorandom 
    (that is, deterministic) numbers based on an internal state 
    that you can set with "random.seed" 
    if you want to get reproducible results.
"""

rand.seed(10)
random1 = rand.random()
rand.seed(10)
random2 = rand.random()

assert random1 == random2

print(rand.randrange(10))

print(rand.randrange(1,7))

upto_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rand.shuffle(upto_ten)
print(upto_ten)

# pick one random choice from a list
print(rand.choice(upto_ten))

# pick a random sample (without duplicates) of size specified by you from a population
lottery_numbers = range(10)
winning_numbers = rand.sample(lottery_numbers, 3)
print(winning_numbers)

import re

re_examples = [
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3 == len(re.split("[ab]", "carbs")),
    "R2D2" == re.sub("-", "2", "R-D-")
    ]

assert all(re_examples)

"""
    One important thing to note is that re.match 
    checks whether the beginning of a string matches a regular expression, 
    while re.search checks whether any part of a string matches a regular expression.
    At some point you will mix these two up and it will cause you grief.
"""

# The zip function transforms multiple iterables 
# into a single iterable of tuples

l1 = ["a", "b", "c"]
l2 = [1, 2, 3]

#zip is lazy, so we have to do something like this 
l3 = [pair for pair in zip(l1,l2)]
print(l3)

# If the lists are different lengths, zip stops as soon as one list ends.
l4 = [pair for pair in zip(l1, [1, 2, 3, 4])]
print(l4)

l5 = [pair for pair in zip([1, 2, 3, 4], l1)]
print(l5)

# unpacking the ziped pairs or anything
letters, numbers = zip(*l3)
print(letters, numbers)
print(letters)
print(numbers)

"""
    The asterisk (*) performs argument unpacking, 
    which uses the elements of pairs as individual arguments to zip. 
    It ends up the same as if you’d called:
        letters, numbners = zip(("a", 1),("b", 2),("c", 3))
"""

# You can use argument unpacking with any function
def adds(a, b): return a + b
assert adds(1, 2) == 3

try:
    adds([1, 2])
except TypeError:
    print("adds expects two inputs")

# neat trick
assert adds(*[1, 2]) == 3
















