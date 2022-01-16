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
    """
    returns summation of element-wise squares
    v_1*v_1.....v_n*v_n
    """
    return dot(v, v)

assert sum_of_squares([1, 1, 1]) == 3
assert sum_of_squares([1, 2, 3]) == 14

import math
def magnitude(v: Vector) -> float:
    """returns magnitude (or length) of the vector"""
    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5
assert magnitude([1, 2, 3, 1, 3, 1]) == 5 

def squared_distance(v: Vector, w: Vector) -> float:
    """computes summation of (v_i - w_i)**2 for all elements"""
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """computes distance between two vectors"""
    return magnitude(subtract(v, w))

assert distance([6, 8], [3, 4]) == 5

### Matrices ###

Matrix = List[List[float]]

A = [[1, 2, 3],
     [4, 5, 6]]     # A has 2 rows and 3 columns

B = [[1, 2],
     [3, 4],
     [5, 6]]        # B has 3 rows and 2 columns

from typing import Tuple

def shape(A: Matrix) -> Tuple:
    """
    Parameters
    ----------
    A : Matrix

    Returns
    -------
    Tuple
        (# of rows in A, # of columns in A).
    """
    assert A, "empty matrix"
    return (len(A), len(A[0]) if A else 0)

assert shape([[]])
assert shape([[1, 2], [3,4]]) == (2, 2)

def get_row(A: Matrix, i: int) -> Vector:
    """
    

    Parameters
    ----------
    A : Matrix
    i : int
        i-th row

    Returns
    -------
    Vector
        i-th row of Matrix A

    """
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """
    

    Parameters
    ----------
    A : Matrix
    j : int
        j-th column

    Returns
    -------
    Vector
        j-th column of Matrix A

    """
    return [ A_i[j] 
            for A_i in A ]

assert get_row(A, 0) == [1, 2, 3]
assert get_column(B, 0) == [1, 3, 5]

from typing import Callable

def make_matrix(num_rows: int,
                num_columns: int,
                entry_fx: Callable[[int, int], float]) -> Matrix:
    """
    

    Parameters
    ----------
    num_rows : int
        number of rows in final Matrix.
    num_columns : int
        number of columns in final Matrix.
    entry_fx : Callable[[int, int], float]
        function of generate A[i][j] element of Matrix A, given i, j.

    Returns
    -------
    Matrix
        Matrix A whose element A[i][j] is entry_fx(i, j) .

    """
    return [[entry_fx(i, j)
            for j in range(num_columns)]
            for i in range(num_rows)
            ]

def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(identity_matrix(5))

"""
    Why Matrices are important:
        1. A Matrix can be used to represent a dataset
        consisting multiple vectors,
        each row being a vector.
        Example: 
            if we had 1000 people with height, weight, age
            we could put them in a 1000 x 3 matrix
        
        2. We can use n x k matrix to represent a linear function
        that maps k-dimensional vectors to n-dimensional vectors
        
        3. Matrices can be used to represent binary relationships 
        between pairs(i, j).
        Example:
            A[i][j] = 1 can represent presence of an edge
            between node i and node j in a graph, else zero
            to represent absence of an edge.
        
        Use numpy for vectors and matrices.
"""





























