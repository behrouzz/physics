# https://www.omnicalculator.com/physics/gravitational-time-dilation
"""
SPECIAL
dt  : Time that has passed as measured by a stationary observer (relative time)
dt_ : Time that has passed as measured by the traveling observer
------------------------------------------------------------------
GENERAL
dt_ : Time interval affected by gravity
dt  : Time interval uninfluenced by gravity (infinite distance)
r   : Distance from the center of object causing the gravitational dilation
"""

import numpy as np
from matplotlib import pyplot as plt
from astropy import units as u
from astropy.constants import c, G, M_sun, R_sun, au
import spiceypy as sp

def mag(x):
    return np.linalg.norm(np.array(x))


def special_time_dilation(v, dt):
    dt_ = dt * np.sqrt( 1 - (v**2)/(c**2) )
    return dt_


def general_time_dilation(M, r, dt):
    dt_ = dt * np.sqrt( 1 - (2*G*M)/(r*(c**2)) )
    return dt_



adr = 'C:/Users/H21/Desktop/Desktop/Behrouz/Astronomy/kernels/'
sp.furnsh(adr+'de440s.bsp')
sp.furnsh(adr+'naif0012.tls')
et = sp.str2et('2023-07-01')
state, lt = sp.spkez(targ=399, et=et, ref='J2000', abcorr='NONE', obs=10)
pos = state[:3]
vel = state[3:]
sp.kclear()

speed = mag(vel) * (u.km/u.s)

delta_t = 86400*u.s

# Earth wrt Sun
dt_ = special_time_dilation(speed, dt=delta_t)
print('SPECIAL - Earth wrt Sun:', dt_)

#print(delta_t - dt_)

dt_ei = general_time_dilation(M_sun, au, dt=delta_t)
print('GENERAL - Earth wrt infini:', dt_ei)
dt_si = general_time_dilation(M_sun, R_sun, dt=delta_t)
print('GENERAL - Sun wrt infini:', dt_si)

print(dt_ei-dt_si)

