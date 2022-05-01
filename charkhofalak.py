import numpy as np
from datetime import datetime, timedelta
from astropy.units import Unit as u
from astropy.constants import G, M_earth, R_earth
import matplotlib.pyplot as plt
from hypatie.transform import unit, mag

gx = 0
gy = - ((G * M_earth) / R_earth**2).value
g = np.array([gx, gy]) * u('m/s2')
m = 70 * u('kg')
w = (m*g).to('N')
v0 = np.array([10, -5]) * u('m/s')
p0 = np.array([-100, 0]) * u('m')
dt = 0.01 * u('s')

pos = []
p = p0
v = v0
t = 0
for i in range(1000):
    #t = t + dt.value
    #uv = unit(p.value)
    #f_ext = -abs(w[1].value)*uv * u('N')
    a_ext = v**2 / (100*u('m'))
    f_ext = m * a_ext
    #print(f_ext)
    f = w + f_ext
    v = v + (f/m)*dt
    p = p + v*dt
    pos.append(p)
    
x = [i.value[0] for i in pos]
y = [i.value[1] for i in pos]

fig, ax = plt.subplots()
ax.scatter(x=[-100], y=[0], c='r') # start
ax.scatter(x=[0], y=[0], c='k', marker='+') # origin of frame
ax.scatter(x, y, alpha=0.5)
plt.show()
