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
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.constants import c, G, M_sun, R_sun, au
import spiceypy as sp
from datetime import datetime, timedelta


def mag(x):
    return np.linalg.norm(np.array(x))


def special_time_dilation(v, dt):
    dt_ = dt * np.sqrt( 1 - (v**2)/(c**2) )
    return dt_


def general_time_dilation(M, r, dt):
    dt_ = dt * np.sqrt( 1 - (2*G*M)/(r*(c**2)) )
    return dt_


def get_dilation(ts):
    adr = 'C:/Users/H21/Desktop/Desktop/Behrouz/Astronomy/kernels/'
    sp.furnsh(adr+'de440s.bsp')
    sp.furnsh(adr+'naif0012.tls')
    delta_t = 1*u.s

    special = []
    general = []

    for t in ts:

        et = sp.str2et(t)
        
        state, lt = sp.spkez(targ=399, et=et, ref='J2000', abcorr='LT', obs=10)
        pos = state[:3]
        r = mag(pos) * u.km
        dt_gr = general_time_dilation(M_sun, r, dt=delta_t)

        state, lt = sp.spkez(targ=399, et=et, ref='J2000', abcorr='LT', obs=0)
        vel = state[3:]        
        speed = mag(vel) * (u.km/u.s)
        #print(speed)
        dt_sr = special_time_dilation(speed, dt=delta_t)

        special.append(dt_sr)
        general.append(dt_gr)

    sp.kclear()

    special = np.array([i.value for i in special])
    general = np.array([i.value for i in general])
    
    return special, general

days = 365 * 5
dates = [datetime(2020,1,1,12,0,0) + timedelta(days=i) for i in range(days)]

ts = [i.isoformat().replace('T', ' ') + ' UTC' for i in dates]

special, general = get_dilation(ts)

total = (1-special) + (1-general)

fig, ax = plt.subplots()
#plt.plot(dates, total)
ax.plot(dates, special, 'b')
ax.plot(dates, general, 'r')
#ax.plot(dates, general - special)
plt.grid()
plt.show()
