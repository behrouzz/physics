import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.time import Time
from astropy.constants import c, G, M_sun, R_sun, au
import spiceypy as sp
from datetime import datetime, timedelta


def mag(x):
    return np.linalg.norm(np.array(x))


def special_time_dilation(v, dt):
    dt_ = dt / np.sqrt( 1 - (v**2)/(c**2) )
    return dt_


def general_time_dilation(M, r, dt):
    #dt_ = dt * np.sqrt( 1 - (2*G*M)/(r*(c**2)) )
    rs = (2*G*M) / (c**2)
    dt_ = dt / np.sqrt( 1 - (rs/r) )
    return dt_


def orbital_time_dilation(M, r, dt):
    rs = (2*G*M) / (c**2)
    dt_ = dt / np.sqrt( 1 - 1.5*(rs/r) )
    return dt_

def get_dilation(ts):
    adr = 'C:/Users/H21/Desktop/Desktop/Behrouz/Astronomy/kernels/'
    sp.furnsh(adr+'de440s.bsp')
    sp.furnsh(adr+'naif0012.tls')
    delta_t = 1*u.s

    special = []
    general = []
    orbital = []

    for t in ts:

        et = sp.str2et(t)
        
        state, lt = sp.spkez(targ=399, et=et, ref='J2000', abcorr='LT', obs=10)
        pos = state[:3]
        r = mag(pos) * u.km
        dt_gr = general_time_dilation(M_sun, r, dt=delta_t)
        dt_or = orbital_time_dilation(M_sun, r, dt=delta_t)

        state, lt = sp.spkez(targ=399, et=et, ref='J2000', abcorr='LT', obs=0)
        vel = state[3:]        
        speed = mag(vel) * (u.km/u.s)
        #print(speed)
        dt_sr = special_time_dilation(speed, dt=delta_t)

        special.append(dt_sr)
        general.append(dt_gr)
        orbital.append(dt_or)

    sp.kclear()

    special = np.array([i.value for i in special])
    general = np.array([i.value for i in general])
    orbital = np.array([i.value for i in orbital])
    
    return special, general, orbital


days = 365 * 5
dates = [datetime(2020,1,1,12,0,0) + timedelta(days=i) for i in range(days)]

# with formula
# ------------
ts = [i.isoformat().replace('T', ' ') + ' UTC' for i in dates]

special, general, orbital = get_dilation(ts)

dt_sp = special - 1
dt_ge = general - 1
total = 1 + (dt_sp + dt_ge)

#total = (1-special) + (1-general)

# with astropy
# ------------
dates2 = [i+timedelta(seconds=1) for i in dates]
dts = (Time(dates2, scale='utc').tcb - Time(dates, scale='utc').tcb).sec



fig, ax = plt.subplots()

ax.plot(dates, total, c='k')
##ax.plot(dates, special, c='b')
##ax.plot(dates, general, c='r')
ax.plot(dates, orbital, c='r')
ax.scatter(dates, dts, s=5, c='g') #astropy

ax.ticklabel_format(axis="y", useOffset=False, style='plain')
plt.grid()
plt.show()
