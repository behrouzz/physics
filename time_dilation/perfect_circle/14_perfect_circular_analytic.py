import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.constants import c, G, M_sun, R_sun, M_earth, R_earth, au


##rs = (2*G*M_sun) / (c**2)
##ini = (rs/au).value

rr = np.linspace(0.1, 5, 10000)
radiuses = rr * au

sp_over_ge = []
for r in radiuses:
    z = ((G*M_sun)/(r*(c**2)))
    sp_over_ge.append(np.sqrt(1-2*z) / np.sqrt(1-z))

sp_over_ge = np.array(sp_over_ge)



fig, ax = plt.subplots()
ax.scatter(rr, sp_over_ge, s=2)
ax.ticklabel_format(axis="y", useOffset=False, style='plain')
plt.grid()
plt.show()

"""
the relative gravitational time dilation between two points equals
to the time dilation due to velocity needed to climb from the lower
point to the higher.

v_esc = sqrt((2*G*M)/(r*c**2))
"""
