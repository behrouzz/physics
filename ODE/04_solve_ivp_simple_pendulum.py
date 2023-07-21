import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def fun(t, s):
    th = s[0]
    thp = s[1]
    thpp = -(g/l)*np.sin(s[0])
    return thp, thpp

l = 10
g = 9.8
th0 = np.pi/4
thp0 = 0

t = np.arange(0, 10.01, 0.01)
t_span = [t[0], t[-1]]
y0 = [th0, thp0] 

sol = solve_ivp(fun=fun,
                t_span=t_span,
                y0=y0,
                t_eval=t)

theta = sol.y[0]
theta_p = sol.y[1]

fig, ax = plt.subplots(2,1)
ax[0].plot(sol.t, theta, c='b')
ax[0].plot(sol.t, theta_p, c='r')
ax[0].set_xlabel('t')
ax[0].set_ylabel('th(blue) | thp(red)')
ax[1].plot(theta, theta_p, c='g')
ax[1].set_xlabel('th')
ax[1].set_ylabel('thp')
plt.show()
