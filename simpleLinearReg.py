#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""



Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info
    !git branch --show-current

*********************************

#-------------------------------------------------------------------------------
print("-----------------------------------------------------------------------")

"""


def predict(alpha: float,
            beta: float,
            x_i: float) -> float:
    return beta * x_i + alpha

def error(alpha: float,
          beta: float,
          x_i: float,
          y_i: float) -> float:
    """
    The error from predicting beta * x_i + alpha
    when the actual value is y_i
    """
    return predict(alpha, beta, x_i) - y_i

from linearAlgebra import Vector

def sum_of_sq_errors(alpha: float,
                     beta: float,
                     x: Vector,
                     y: Vector) -> float:
    return sum( error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y)
              )

from typing import Tuple
from statss import correlation, standard_deviation, mean

def least_squares_fit(x: Vector,
                      y: Vector) -> Tuple[float, float]:
    """
    Given two vectos x and y,
    finds the least-squares values of alpha and beta
    """
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta

x = [i for i in range(-100, 110, 10)]
y = [3 * i - 5 for i in x]

# Should find that y = 3x - 5
(_, __) = least_squares_fit(x, y)
print(_, __)
assert (_, __) == (-5, 3)

from statss import num_friends_good, daily_minutes_good

alpha, beta = least_squares_fit(num_friends_good, daily_minutes_good)
print(f"  alpha : {alpha:.3f} \n  beta  : {beta:.3f}")
assert 22.9 < alpha < 23.0
assert 0.9 < beta < 0.905

# for plotting graphs
import plotly.express as px
import plotly.graph_objects as go
# below three lines helps choose where to render the plotly plots
# it needs plotly dependency kaleido installed for in-IDE rendering as svg
import plotly.io as pio
pio.renderers.default = 'svg'
#pio.renderers.default = 'browser'

# plotly figure setup
fig = go.Figure()
fig.add_trace(
                go.Scatter(
                            x = num_friends_good,
                            y = daily_minutes_good,
                            mode = 'markers',
                            showlegend = False
                          )
             )
fig.add_trace(
                go.Scatter(
                            name = "line of least-squares-regression from scratch",
                            x = num_friends_good,
                            y = [beta * _ + alpha for _ in num_friends_good],
                            mode = 'lines'
                          )
             )

# plotly figure layout
fig.update_layout(
                  title = 'Simple Linear Regression Model',
                  xaxis_title = 'num_friends_good',
                  yaxis_title = 'daily_minutes_good'
                 )
fig.update_layout(legend = dict(
                                orientation = 'h',
                                yanchor = 'top',
                                y = -0.15,
                                xanchor = 'left',
                                x = 0))

fig.show()

from statss import de_mean

def total_sum_of_squares(y: Vector) -> float:
    """the total squared variation of y_i's from their mean"""
    return sum( v ** 2 for v in de_mean(y) )

def r_squared(alpha: float,
              beta: float,
              x: Vector,
              y: Vector) -> float:
    """
    the fraction of variation in y captured by the model, which equals
    1 - the fraction of variation in y not captured in the model
    """
    return 1.0 - ( sum_of_sq_errors(alpha, beta, x, y) /
                   total_sum_of_squares(y) 
                 )

rsq = r_squared(alpha, beta, num_friends_good, daily_minutes_good)
print("r-squared: ", rsq)
assert 0.328 < rsq < 0.330




def main():
    import random
    import tqdm
    from gradient import gradient_step
    
    num_epochs = 100000
    random.seed(0)
    
    # choose random alpha and beta values to start with
    guess = [random.random(), random.random()]
    
    learning_rate = 0.00001
    
    with tqdm.trange(num_epochs) as t:
        for _ in t:
            alpha, beta = guess
            
            # partial derivative of loss with respect to alpha
            grad_a = sum(2 * error(alpha, beta, x_i, y_i)
                         for x_i, y_i in zip(num_friends_good,
                                             daily_minutes_good)
                        )
            
            # partial derivative of loss with respect to beta
            grad_b = sum(2 * error(alpha, beta, x_i, y_i) * x_i
                         for x_i, y_i in zip(num_friends_good,
                                             daily_minutes_good)
                        )
            
            # compute loss to stick in the tqdm description
            loss = sum_of_sq_errors(alpha, beta,
                                    num_friends_good,
                                    daily_minutes_good
                                   )
            t.set_description(f"loss: {loss:.3f}")
            
            # finally, update the guess
            guess = gradient_step(guess, [grad_a, grad_b], - learning_rate)
    
    # we should get the same results as we did with the formula
    
    alpha, beta = guess
    print( "alpha and beta calculations using gradient descent" )
    print(f"  alpha : {alpha:.3f} \n  beta  : {beta:.3f}")
    assert 22.9 < alpha < 23.0
    assert 0.9 < beta < 0.905
    





"""
    When we import a module,
    internally Python executes everything inside the module. 
    To avoid it, we can tell the Python interpreter
    that some code needs to run only when executed as a script, and not imported. 
    To achieve that, we put our code inside the following construction:
    
            if __name__ == "__main__":
                code
    
    this "code" will not run when the script is imported,
    but will run if the script is executed.
"""

if __name__ == "__main__":
    main()



















