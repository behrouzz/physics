# https://www.omnicalculator.com/physics/gravitational-time-dilation
"""
dt_ : Time interval affected by gravity
dt  : Time interval uninfluenced by gravity (infinite distance)
r   : Distance from the center of object causing the gravitational dilation
"""

import numpy as np
from matplotlib import pyplot as plt
from astropy import units as u
from astropy.constants import c, G, M_sun, R_sun, au


def time_dilation(M, r, dt=1*u.s):
    dt_ = dt * np.sqrt( 1 - (2*G*M)/(r*(c**2)) )
    return dt_

dt = 86400*365.25*u.s

dt_ = time_dilation(M_sun, au, dt=dt)

dt_earth = dt - dt_
print(dt_earth)

dt_ = time_dilation(M_sun, R_sun, dt=dt)
dt_sun = dt - dt_
print(dt_sun)

diff = dt_sun - dt_earth
print(diff)
