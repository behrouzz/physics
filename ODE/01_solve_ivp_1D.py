#https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.06-Python-ODE-Solvers.html

"""
dS(t) / dt = F(t, S(t))
S(t0) = S0

Example:
--------
Consider the ODE:

dS(t) / dt = 5 * cos(t)

with an initial value of S0 = 0.

Use solve_ivp to approximate the solution to this initial value problem
over the interval [0,pi].
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def F(t, s):
    return 5*np.cos(t)

t_eval = np.arange(0, np.pi, 0.1)

sol = solve_ivp(F, [0, np.pi], [0], t_eval=t_eval)

plt.plot(sol.t, sol.y[0])
plt.xlabel('t')
plt.ylabel('S(t)')
plt.show()
