# https://www.khanacademy.org/science/physics/special-relativity/lorentz-transformation/v/algebraically-manipulating-lorentz-transformation

import numpy as np
from astropy import units as u
from astropy.constants import c


def lorentz_transformation(v, x, ct):
    beta = v / c
    gamma = 1 / np.sqrt(1 - beta**2)
    x_ = gamma * (x - beta*ct)
    ct_ = gamma * (ct - beta*x)
    return x_, ct_

def lorentz_transformation_another(v, x, t):
    beta = v / c
    gamma = 1 / np.sqrt(1 - beta**2)
    x_ = gamma * (x - v*t)
    t_ = gamma * (t - (v/c**2)*x)
    return x_, t_


v = 0.5 * c
x = 1 * u.m
ct = 1 * u.m

x_, ct_ = lorentz_transformation(v, x, ct)
print('x_ :', x_)
print('ct_:', ct_)

t = ct / c
x_, t_ = lorentz_transformation_another(v, x, t)
print('x_ :', x_)
print('t_ :', t_)
