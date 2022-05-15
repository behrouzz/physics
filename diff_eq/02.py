# https://www.deboecksuperieur.com/site/328907
# https://math.libretexts.org/Bookshelves/Calculus/Book%3A_Calculus_(Guichard)/17%3A_Differential_Equations/17.01%3A_First_Order_Differential_Equations#:~:text=A%20first%20order%20differential%20equation,%2C%20y%2C%20and%20%CB%99y.

"""
dy / dt = t - y
y(0) = 2


sol.t
-----
the times at which the solver found values

sol.y
-----
a 2-D array. Each row of sol.y will be the solution to one of the dependent
variables -- since this problem has a single differential equation with a
single initial condition, there will only be one row.
"""

from scipy.integrate import solve_ivp
import numpy as np

def fun(t, y):
    return t - y

sol = solve_ivp(fun=fun , t_span=[0, 15], y0=[2], rtol=1e-5)

# Plot

import matplotlib.pyplot as plt

plt.plot(sol.t, sol.y[0], 'k--s')
plt.show()
