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


def orbital_time_dilation(M, r, dt):
    rs = (2*G*M) / (c**2)
    dt_ = dt / np.sqrt( 1 - 1.5*(rs/r) )
    return dt_


r = au

dt_gr = general_time_dilation(M_sun, r, dt=1*u.s)
print('General:', dt_gr.value-1)

speed = np.sqrt((G*M_sun)/r)
dt_sr = special_time_dilation(speed, dt=1*u.s)
print('Special:', dt_sr.value-1)

print('Gen+Spe:', (dt_sr.value-1) + (dt_gr.value-1))

dt_or = orbital_time_dilation(M_sun, r, dt=1*u.s)
print('Orbital:', dt_or.value-1)

