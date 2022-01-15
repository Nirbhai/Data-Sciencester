#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Algebra is a way of seeing and thinking.
For instance:
    
    -> if you have the heights, weights and ages of a large number of people, 
    you can treat your data as three-dimensional vectors [height, weight, age].
    
    -> if you're teaching a class which has four exams, you can treat student grades
    as a four dimensional vector [exam1, exam2, exam3, exam4]

Such a way of looking at things or thinking of such collections and their instances
as vectors, sometimes helps in figuring out how to manipulate the data, and
greatly helps in talking about it with a fellow or reason about it in your own head.


Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info -e
    !git branch -a

*********************************


"""

from typing import List

Vector = List[float]

height_weight_age_vector = [70,     # inches
                            170,    # pounds
                            40 ]    # years

grades_vector = [95,    # exam1
                 80,    # exam2
                 89,    # exam3
                 68]    # exam4

# vector arithmatic

def add(v: Vector, w: Vector) -> Vector:
    """adds corresponding elements of same length vectors"""
    assert len(v) == len(w), "vectors must be of same length for addition"
    return [ v_i + w_i for v_i, w_i in zip(v, w) ]


assert add([1, 2, 4], [4, 2, 1]) == [5, 4, 5]

def subtract(v: Vector, w: Vector) -> Vector:
    """ subtracts corresponding elements of same length vectors"""
    assert len(v) == len(w), "vectors must be of same length for subtraction"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([3, 4, 5], [1, 1, 1]) == [2, 3, 4]

def vector_sum(vectors: List[Vector]) -> Vector:
    """adds corresponding elements of all vectors in the list"""
    # check the list is not empty
    assert vectors, "no vectors provided"
    
    # check all vectors of same size
    size = len(vectors[0])
    assert all(size == len(vec) for vec in vectors), "vectors not of same size"
    
    # the i-th element of the result is sum of i-th element of all vectors
    return [sum(vec[i] for vec in vectors)
            for i in range(size)]

assert vector_sum([[1, 2], [3, 4], [5, 0]]) == [9, 6]

def scaler_multiply(v: Vector, s) -> Vector:
    """multiply each element of vector v with scaler s"""
    return [s * v_i for v_i in v]

assert scaler_multiply([1, 2, 3], 3) == [3, 6, 9]

def vector_mean(vectors: List[Vector]) -> Vector:
    """computes mean of a list of same-sized vectors"""
    # check the list is not empty
    assert vectors, "no vectors provided"
    
    # check all vectors of same size
    size = len(vectors[0])
    assert all(size == len(vec) for vec in vectors), "vectors not of same size"
    
    return scaler_multiply(vector_sum(vectors), 1/len(vectors))

assert vector_mean([[1,2],[2,1],[0,0]]) == [1, 1]

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

def dot(v: Vector, w: Vector) -> float:
    """
    returns summation of element-wise product
    v_1*w_1 + .... v_n*W_n
    """
    assert len(v) == len(w), "vectors must be of same length for dot product"
    
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 1, 1], [2, 2, 2]) == 6
assert dot([1, 1, 1], [1, 1, 1]) == 3
assert dot([1, 1], [0, 0]) == 0

def sum_of_squares(v: Vector) -> float:
    










































