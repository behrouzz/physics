# https://www.deboecksuperieur.com/site/328907

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def dist(pos_i, pos_j):
    xi, yi = pos_i
    xj, yj = pos_j
    d = np.sqrt((xi-xj)**2 + (yi-yj)**2)
    return d


def fun(t, s):
    x1, x1p = s[0], s[1]
    y1, y1p = s[2], s[3]

    x2, x2p = s[4], s[5]
    y2, y2p = s[6], s[7]

    x3, x3p = s[8], s[9]
    y3, y3p = s[10], s[11]

    r12 = dist((x1,y1), (x2,y2))
    r13 = dist((x1,y1), (x3,y3))
    r23 = dist((x2,y2), (x3,y3))
    
    x1pp = (x2-x1)/r12**3 + (x3-x1)/r13**3
    y1pp = (y2-y1)/r12**3 + (y3-y1)/r13**3

    x2pp = (x1-x2)/r12**3 + (x3-x2)/r23**3
    y2pp = (y1-y2)/r12**3 + (y3-y2)/r23**3

    x3pp = (x1-x3)/r13**3 + (x2-x3)/r23**3
    y3pp = (y1-y3)/r13**3 + (y2-y3)/r23**3
    
    return x1p,x1pp, y1p,y1pp, x2p,x2pp, y2p,y2pp, x3p,x3pp, y3p,y3pp


t = np.linspace(0, 5, 1000)
t_span = [t[0], t[-1]]

x1p, y1p =  0.5,  0.1
x2p, y2p =  0.1, -0.4
x3p, y3p = -0.6,  0.3

x01, y01 = -1, -0.5
x02, y02 =  1,  0.5
x03, y03 =  0,  1

y0 = [x01,x1p, y01,y1p, x02,x2p, y02,y2p, x03,x3p, y03,y3p]

sol = solve_ivp(fun, t_span, y0, t_eval=t, rtol=1e-9)

x1, y1 = sol.y[0], sol.y[2]
x2, y2 = sol.y[4], sol.y[6]
x3, y3 = sol.y[8], sol.y[10]

plt.axis('equal')
plt.scatter([x01, x02, x03], [y01, y02, y03])
plt.plot(x1, y1, color='blue')
plt.plot(x2, y2, color='black')
plt.plot(x3, y3, color='green')
plt.ylim(-1, 1.7)
plt.show()
