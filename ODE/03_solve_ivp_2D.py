"""
dS(t) / dt = F(t, S(t))
S(t0) = S0

Example:
--------
Let the state of a system be defined by:

       | x(t) |
S(t) = |      |
       | y(t) |

and let the evolution of the system be defined by the ODE:

dS(t)   | 0   t^2 |
----- = |         | * S(t)
 dt     | -t  0   |

Use solve_ivp to solve this ODE for the time interval [0,10] with an
initial value of

     | 1 |
S0 = |   |
     | 1 |
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def F(t, s):
    return np.dot(np.array([[0, t**2], [-t, 0]]), s)

t_eval = np.arange(0, 10.01, 0.01)

sol = solve_ivp(F, [0, 10], [1,1], t_eval=t_eval)

t = sol.t
x = sol.y[0]
y = sol.y[1]

fig, ax = plt.subplots(3,1)

ax[0].plot(t, x)
ax[1].plot(t, y)
ax[2].plot(x, y)
plt.show()
