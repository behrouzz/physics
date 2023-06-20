# https://www.khanacademy.org/science/physics/special-relativity/einstein-velocity-addition/v/applying-einstein-velocity-addition

import numpy as np
from astropy.constants import c



def addition(v, u):
    return (u-v) / (1-(u*v)/c**2)


v = 0.7 * c
u = -0.5 * c

res = addition(v, u)

print(res/c)





