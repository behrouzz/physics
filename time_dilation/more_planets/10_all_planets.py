import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.time import Time
from astropy.constants import c, G, M_sun, R_sun, M_earth, R_earth, au
import spiceypy as sp
from datetime import datetime, timedelta


def mag(x):
    return np.linalg.norm(np.array(x))

def special_time_dilation(v, dt):
    dt_ = dt / np.sqrt( 1 - (v**2)/(c**2) )
    return dt_

def general_time_dilation(M, r, dt):
    rs = (2*G*M) / (c**2)
    dt_ = dt / np.sqrt( 1 - (rs/r) )
    return dt_


def distances(targets, t):
    r = np.zeros(len(targets),)
    for i, targ in enumerate(targets):
        et = sp.str2et(t)
        state, _ = sp.spkez(targ=targ, et=et, ref='J2000', abcorr='LT', obs=399)
        r[i] = mag(state[:3])
    return r * u.km


adr = 'C:/Users/H21/Desktop/Desktop/Behrouz/Astronomy/kernels/'
sp.furnsh(adr+'de440s.bsp')
sp.furnsh(adr+'naif0012.tls')




t = '2020-01-01 00:00:00 UTC'
targets = [10, 1, 2, 301, 399, 4, 5, 6, 7, 8, 9]
masses = np.array(
    [1.9884098713165342e+30, 3.301000636920726e+23, 4.867305814842006e+24,
     7.345789248310684e+22, 5.972168399787243e+24, 6.41690901158174e+23,
     1.898517658780696e+27, 5.684578883448452e+26, 8.681893831562862e+25,
     1.0243062344485564e+26, 1.4615764949133244e+22]
    ) * u.kg

r = distances(targets, t)
r[4] = R_earth

general = [general_time_dilation(masses[i], r[i], 1*u.s).value for i in range(len(targets))]
dt_gr = (np.array(general) - 1).sum()

et = sp.str2et(t)
state, _ = sp.spkez(targ=399, et=et, ref='J2000', abcorr='LT', obs=0)
speed = mag(state[3:]) * (u.km/u.s)
special = special_time_dilation(speed, dt=1*u.s).value
dt_sr = special - 1

dt_total = 1 + dt_gr + dt_sr
print(dt_total)

sp.kclear()


t1 = Time('2020-01-01 12:00:00', scale='utc').tcb
t2 = Time('2020-01-01 12:00:01', scale='utc').tcb

dt_astropy = (t2-t1).sec
print(dt_astropy)


