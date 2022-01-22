#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Frequently when doing data science, 
we’ll be trying to the find the best model for a certain situation. 
And usually “best” will mean something like 
“minimizes the error of its predictions” or 
“maximizes the likelihood of the data.” 
In other words, 
it will represent the solution to some sort of optimization problem.



Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info -e
    !git branch -a

*********************************


"""

from linearAlgebra import Vector, dot

def sum_of_squares(v: Vector) -> float:
    """
    returns summation of element-wise squares
    v_1*v_1.....v_n*v_n
    """
    return dot(v, v)


from typing import Callable

def difference_quotient(f: Callable[[float], float],
                        x: float,
                        h: float) -> float:
    return (f(x + h) - f(x)) / h

def squares(x: float) -> float:
    return x * x

def derivative(x: float) -> float:
    return 2 * x

xs = range(-10,11)
actuals = [ derivative(x) for x in xs ]
estimates = [ difference_quotient(squares, x, h=0.001) for x in xs ]
estimates1 = [ difference_quotient(squares, x, h=5) for x in xs ]
estimates2 = [ difference_quotient(squares, x, h=10) for x in xs ]

# plot to show they're basically the same
import matplotlib.pyplot as plt
plt.title("Actual derviatives vs. Estimates")
plt.plot(xs, actuals, "rx", label = "Actual")                     # red x
plt.plot(xs, estimates2, "b^", label = "Estimates with h = 10")   # blue ^
plt.plot(xs, estimates1, "b*", label = "Estimates with h = 5")    # blue *
plt.plot(xs, estimates, "b+", label = "Estimates with h = .001")  # blue +

plt.legend(loc=2)
plt.show()

"""
    The derivative is the slope of the tangent line at x, f(x), 
    while the difference quotient is the slope of the not-quite-tangent
    line that runs through x + h, f(x + h). 
    As h gets smaller and smaller, 
    the not-quite-tangent line gets closer and closer to the tangent line
    
    The above plot shows this.
"""



def partial_difference_quotient(f: Callable[[Vector], float],
                                v: Vector,
                                i: float,
                                h: float) -> float:
    """ returns the i-th partial difference quotient of "f" at "v"""
    w = [ v_j + (h if j == i else 0)
         for j, v_j in enumerate(v)]
    return ( f(w) - f(v) ) / h

def estimate_gradient(f: Callable[[Vector], float],
                      v: Vector,
                      h: float) -> Vector:
    """computationally very heavy function"""
    return [ partial_difference_quotient(f, v, i, h)
            for i in range(len(v))]

"""
    It’s easy to see that the sum_of_squares function is 
    smallest when its input v is a vector of zeros. 
    But imagine we didn’t know that. 
    Let’s use gradients to find the minimum 
    among all three-dimensional vectors. 
    We’ll just pick a random starting point and 
    then take tiny steps in the opposite direction 
    of the gradient until we reach a point 
    where the gradient is very small.
"""

import random
from linearAlgebra import distance, add, scaler_multiply

def gradient_step(v: Vector,
                  gradient: Vector,
                  step_size: float) -> Vector:
    """Moves "step size" in the "gradient" direction from v"""
    assert len(v) == len(gradient), "vectors not of same size"
    step = scaler_multiply(gradient, step_size)
    return add(v, step)

def sum_of_squares_gradient(v: Vector) -> Vector:
    """the actual gradient of sum_of_squares function"""
    return [ 2 * v_i for v_i in v]

# picking a random starting point
v = [ random.uniform(-10, 10) for i in range(3) ]

for epoch in range(1000):
    grad = sum_of_squares_gradient(v)       # compute the gradient at v
    v = gradient_step(v, grad, -0.01)       # take a -ve gradient step
    print(epoch, v)

assert distance(v, [0, 0, 0]) < 0.001       # v should be close to 0


# x ranges from -10 to 49 and y = 20 * x + 5
inputs = [ (x, 20 * x + 5) for x in range(-50, 50) ]

"""
    In this case we know the parameters of the linear relationship 
    between x and y, 
    but imagine we’d like to learn them from the data. 
    We’ll use gradient descent to find the slope and intercept 
    that minimize the average squared error.
"""

def linear_gradient(x: float,
                    y: float,
                    theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept       # the prediction of the model
    error = predicted - y                   # error = predicted - actual
    #squared_error = error ** 2             # we'll minimze squared error
    grad = [2 * error * x, 2 * error]       # using its gradient
    return grad

from linearAlgebra import vector_mean

# start with random values for intercept and slope
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

learning_rate = 0.001

# After a lot of epochs (what we call each pass through the dataset), 
# we should learn something like the correct parameters
for epoch in range(5000):
    # compute the mean of gradients
    grad = vector_mean([ linear_gradient(x, y, theta) for  x,y in inputs ])
    # take a step in that direction
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta

assert 19.9 < slope < 20.1, f"slope is {slope}, which is not near enough 20"
assert 4.9 < intercept < 5.1, f"intercept is {intercept}, which is not near enough 5"

print (inputs)


from typing import TypeVar, List, Iterator

T = TypeVar('T')    # this allows us type generic functions

def minibatches(dataset: List[T],
                batch_size: int,
                Shuffle: bool = True) -> Iterator[List[T]]:
    """Generates batch_size sized minimatches from the dataset"""
    # start indexes 0, batch_size, 2 * batch_size, ...
    batch_starts = [start for start in range(0, len(dataset), batch_size)]
    
    if Shuffle: random.shuffle(batch_starts)
    
    for start in batch_starts:
        end = start + batch_size
        yield dataset[ start : end ]

# Now we can solve our problem again using minibatches

theta = [ random.uniform(-1,1), random.uniform(-1, 1)]

for epoch in range(1000):
    for batch in minibatches(inputs, batch_size = 20):
        grad = vector_mean([linear_gradient(x, y, theta) for x,y in batch])
        theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta

assert 19.9 < slope < 20.1, f"slope is {slope}, which is not near enough 20"
assert 4.9 < intercept < 5.1, f"intercept is {intercept}, which is not near enough 5"

# Another variation is stochastic gradient descent, 
# in which you take gradient steps based on one training example at a time

theta = [ random.uniform(-1,1), random.uniform(-1, 1)]

for epoch in range(100):
    for x,y in inputs:
        grad = linear_gradient(x, y, theta)
        theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta

assert 19.9 < slope < 20.1, f"slope is {slope}, which is not near enough 20"
assert 4.9 < intercept < 5.1, f"intercept is {intercept}, which is not near enough 5"




























