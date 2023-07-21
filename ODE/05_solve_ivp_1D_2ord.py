"""
https://media.ed.ac.uk/media/Solving+Differential+Equations+in+PythonA+Higher+order+ODEs+with+solve_ivp/1_c8g7fwhw

d2x/dt2 = mu*(1-x**2)*(dx/dt) - x

x0 = 1
xp0 = 0
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def fun(t, s):
    x = s[0]
    xp = s[1]
    xpp = mu*(1-x**2)*xp - x
    return xp, xpp

mu = 0
x0 = 1
xp0 = 0

t = np.linspace(0, 10, 500)
t_span = [t[0], t[-1]]
y0 = [x0, xp0] 

sol = solve_ivp(fun=fun,
                t_span=t_span,
                y0=y0,
                t_eval=t)

x = sol.y[0]
xp = sol.y[1]

fig, ax = plt.subplots(3,1)
ax[0].plot(sol.t, x)
ax[1].plot(sol.t, xp)
ax[2].plot(x, xp)
ax[0].set_xlabel('t')
ax[0].set_ylabel('X(t)')
ax[1].set_xlabel('t')
ax[1].set_ylabel('XP(t)')
ax[2].set_xlabel('X(t)')
ax[2].set_ylabel('XP(t)')
plt.show()
