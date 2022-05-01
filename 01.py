import numpy as np
from funcs import drag
import matplotlib.pyplot as plt


g = 9.80665   # m/s2
m = 1         # kg
w = m*g       # N
rho   = 1.225 # kg/m3
R = 1      # m
mu = 2e-5     #  kg /(m s)
#================================

# Without air resistance
v = 0         # m/s
z = 100       # m

ts = [0] 
zs = [z]
dt = 0.001
for i in range(20000):
    F = -w + drag(rho, R, v, mu)
    a = F/m
    v = v + a*dt
    z = z + v*dt
    zs.append(z)
    ts.append(ts[-1]+dt)

zs1 = np.array(zs)
ts1 = np.array(ts)
#================================
# With air resistance
v = 0         # m/s
z = 100       # m

ts = [0] 
zs = [z]
dt = 0.001
for i in range(20000):
    F = -w
    a = F/m
    v = v + a*dt
    z = z + v*dt
    zs.append(z)
    ts.append(ts[-1]+dt)

zs2 = np.array(zs)
ts2 = np.array(ts)
#================================

fig, ax = plt.subplots()
ax.scatter(ts1, zs1, s=1, c='b', alpha=0.25)
ax.scatter(ts2, zs2, s=1, c='r', alpha=0.25)
plt.show()
