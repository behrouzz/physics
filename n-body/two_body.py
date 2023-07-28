# https://orbital-mechanics.space/the-n-body-problem/two-body-inertial-numerical-solution.html
# https://github.com/bryanwweber/orbital-mechanics-notes/blob/main/the-n-body-problem/scripts/two-body-inertial-numerical-solution.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D


def absolute_motion(t, y):
    """Calculate the motion of a two-body system in an inertial reference frame.

    The state vector ``y`` should be in the order:

    1. Coordinates of $m_1$
    2. Coordinates of $m_2$
    3. Velocity components of $m_1$
    4. Velocity components of $m_2$
    """
    # Get the six coordinates for m_1 and m_2 from the state vector
    R_1 = y[:3]
    R_2 = y[3:6]

    # Fill the derivative vector with zeros
    ydot = np.zeros_like(y)

    # Set the first 6 elements of the derivative equal to the last
    # 6 elements of the state vector, which are the velocities
    ydot[:6] = y[6:]

    # Calculate the acceleration terms and fill them in to the rest
    # of the derivative array
    r = np.sqrt(np.sum(np.square(R_2 - R_1)))
    ddot = G * (R_2 - R_1) / r ** 3
    ddotR_1 = m_2 * ddot
    ddotR_2 = -m_1 * ddot

    ydot[6:9] = ddotR_1
    ydot[9:] = ddotR_2
    return ydot

#---------------------------------------------
G = 6.67430e-20   # km**3/(kg * s**2)
m_1 = m_2 = 1e26  # kg

R_1_0 = np.array((0, 0, 0))  # km
R_2_0 = np.array((3000, 0, 0))  # km
dotR_1_0 = np.array((10, 20, 30))  # km/s
dotR_2_0 = np.array((0, 40, 0))  # km/s

y_0 = np.hstack((R_1_0, R_2_0, dotR_1_0, dotR_2_0))

# [section-2]
X_1 = y_0[0]
Y_1 = y_0[1]
Z_1 = y_0[2]
X_2 = y_0[3]
Y_2 = y_0[4]
Z_2 = y_0[5]

r = np.sqrt((X_2 - X_1) ** 2 + (Y_2 - Y_1) ** 2 + (Z_2 - Z_1) ** 2)

ddotX_1 = G * m_2 * (X_2 - X_1) / r ** 3
ddotY_1 = G * m_2 * (Y_2 - Y_1) / r ** 3
ddotZ_1 = G * m_2 * (Z_2 - Z_1) / r ** 3
ddotX_2 = -G * m_1 * (X_2 - X_1) / r ** 3
ddotY_2 = -G * m_1 * (Y_2 - Y_1) / r ** 3
ddotZ_2 = -G * m_1 * (Z_2 - Z_1) / r ** 3

#---------------------------------------------


t_0 = 0  # seconds
t_f = 480  # seconds
t_points = np.linspace(t_0, t_f, 1000)

sol = solve_ivp(absolute_motion, [t_0, t_f], y_0, t_eval=t_points)

y = sol.y.T
R_1 = y[:, :3]  # km
R_2 = y[:, 3:6]  # km
V_1 = y[:, 6:9]  # km/s
V_2 = y[:, 9:]  # km/s
barycenter = (m_1 * R_1 + m_2 * R_2) / (m_1 + m_2)  # km



from hypatie.animation import Body, play
from datetime import datetime, timedelta


t0 = datetime.utcnow()
ts = [t0 + timedelta(days=i) for i in range(int(1000))]

sun = Body('Sun', R_1, ts)
earth = Body('Earth', R_2, ts)
b = Body('Venus', barycenter, ts)


anim = play(bodies=[sun, earth, b],
              names=['Sun', 'Earth', 'b'],
              colors=['r', 'b', 'k'],
              sizes=[10, 10, 2],
              path=True,
              #title='Pentagram (petals) of Venus',
              interval=1)

plt.show()


