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
for r in radiuses:
    dt_gr = general_time_dilation(M_sun, r, dt=1*u.s)
    general = dt_gr.value-1
    speed = np.sqrt((G*M_sun)/r)
    dt_sr = special_time_dilation(speed, dt=1*u.s)
    special = dt_sr.value-1
    print(special/general)
    gen_p_spe.append(general + special)
    dt_or = orbital_time_dilation(M_sun, r, dt=1*u.s)
    orbital.append(dt_or.value-1)

gen_p_spe = np.array(gen_p_spe)
orbital = np.array(orbital)

##fig, ax = plt.subplots(2,1)
##ax[0].scatter(rr, orbital, c='b', s=5, alpha=0.5)
##ax[1].scatter(rr, gen_p_spe, c='r', s=5, alpha=0.5)
##ax[0].grid()
##ax[1].grid()
##plt.show()

plt.scatter(rr, orbital-gen_p_spe, s=2)
plt.grid()
plt.show()
