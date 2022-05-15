# https://www.deboecksuperieur.com/site/328907
"""
Imagine this differential equaytion of the first order:

dy / dt = -y   with   y(0) = 3

who has the exact solution y = 3 * e**(-t)

We want to solve it numerically for values of t between 0 and 1.
"""

from scipy.integrate import solve_ivp
import numpy as np

def fun(t, y):
    return -y

y0 = [3]
sol = solve_ivp(fun , [0, 1], y0)

print("sol.t :", sol.t)
print("sol.y :", sol.y)
print("solution exacte : y(1)=", 3/np.exp(1))
