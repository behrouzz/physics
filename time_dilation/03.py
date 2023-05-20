# https://www.omnicalculator.com/physics/gravitational-time-dilation
"""
dt_ : Time interval affected by gravity
dt  : Time interval uninfluenced by gravity (infinite distance)
r   : Distance from the center of object causing the gravitational dilation
--------------------------------------------
dt  : Time that has passed as measured by a stationary observer (relative time)
dt_ : Time that has passed as measured by the traveling observer
"""

import numpy as np
from matplotlib import pyplot as plt
from astropy import units as u
from astropy.constants import c, G, M_sun, R_sun, au
import spiceypy as sp

def mag(x):
    return np.linalg.norm(np.array(x))


def special_time_dilation(v):
    dt_DIVdt = np.sqrt( 1 - (v**2)/(c**2) )
    return dt_DIVdt


def general_time_dilation(M, r):
    dt_DIVdt = np.sqrt( 1 - (2*G*M)/(r*(c**2)) )
    return dt_DIVdt



sp.furnsh('de440s.bsp')
sp.furnsh('naif0012.tls')
et = sp.str2et('2023-07-01')
state, lt = sp.spkez(targ=399, et=et, ref='J2000', abcorr='NONE', obs=10)
pos = state[:3]
vel = state[3:]
sp.kclear()

speed = mag(vel) * (u.km/u.s)


dt_ = special_time_dilation(speed)
print(dt_)

dt_ = general_time_dilation(M_sun, au)
print(dt_)
