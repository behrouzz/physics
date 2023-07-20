"""
dS(t) / dt = F(t, S(t))
S(t0) = S0

Example:
--------
Consider the ODE:

d/dt(dth/dt) = sin(th)

with an initial value of th=pi/6.

Use solve_ivp to approximate the solution to this initial value problem
over the interval [0,pi].
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def F(t, s):
    thp = s
    thpp = 
    return -s

t_eval = np.arange(0, 1.01, 0.01)

sol = solve_ivp(F, [0, 1], [1], t_eval=t_eval)

plt.plot(sol.t, sol.y[0])
plt.xlabel('t')
plt.ylabel('S(t)')
plt.show()
