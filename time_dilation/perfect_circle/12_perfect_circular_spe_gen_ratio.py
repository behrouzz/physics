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

rr = np.linspace(0.1, 5, 10000)
radiuses = rr * au


gen_p_spe = []
orbital = []
spe_gen_ratio = []
for r in radiuses:
    dt_gr = general_time_dilation(M_sun, r, dt=1*u.s)
    general = dt_gr.value-1
    speed = np.sqrt((G*M_sun)/r)
    dt_sr = special_time_dilation(speed, dt=1*u.s)
    special = dt_sr.value-1
    spe_gen_ratio.append(dt_sr.value/dt_gr.value)
    gen_p_spe.append(general + special)
    dt_or = orbital_time_dilation(M_sun, r, dt=1*u.s)
    orbital.append(dt_or.value-1)

gen_p_spe = np.array(gen_p_spe)
orbital = np.array(orbital)
spe_gen_ratio = np.array(spe_gen_ratio)



fig, ax = plt.subplots()
ax.scatter(rr, spe_gen_ratio, s=2)
ax.ticklabel_format(axis="y", useOffset=False, style='plain')
plt.grid()
plt.show()
