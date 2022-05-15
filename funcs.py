"""
In ordinary temperature:

rho_air   = 1.225 * u('kg/m3')
rho_water = 997   * u('kg/m3')
mu_air    = 2e-5  * u('kg /(m s)')
mu_water  = 10e-3 * u('kg /(m s)')

------------------------------
when dt --> 0 :
f(t+dt) = f(t) + f'(t)*dt
"""
#https://www.deboecksuperieur.com/site/328907
import numpy as np
#from astropy.constants import G, M_earth, R_earth
#from astropy.units import Unit as u

def reynolds_number(rho, v, D, mu):
    """
    Arguments
    ---------
        rho : density of the fluid
        v   : speed of the object relative to the fluid
        D   : equivalent diameter of the object
        mu  : dynamic viscosity of the fluid

    Returns
    -------
        Reynolds number
    """
    Re = (rho * v * D) / mu
    return Re


def drag(rho, R, v, mu):
    """
    Drag (fluid resistance) force on an object wrt surrounding fluid
    Arguments
    ---------
        rho : density of the fluid
        R   : equivalent diameter of the object
        v   : speed of the object relative to the fluid
        mu  : dynamic viscosity of the fluid

    Returns
    -------
        drag force
    """
    Re = reynolds_number(rho, v, 2*R, mu)
    pi = 3.141592653589793
    if Re <= 1: # laminaire
        F = 6 * pi * mu * R * v
    elif Re >= 1000: # turbulent
        F = 0.25 * rho * pi*R**2 * v**2
    else:
        raise Exception('Complicated case!')
    #F = F.to('N')
    return F


def get_alpha(R, rho_b, rho, h, g=9.81):
    """
    R     : radius of the ball (m)
    rho_b : density of the ball
    rho   : density of the air
    h     : initial height
    g     : acceleration
    """
    return (3*rho)/(16*rho_b*R*g)


def get_vlim(R, rho_b, rho, h, g=9.81):
    """
    Get Terminal velocity
    (maximum speed attainable by an object as it falls through a fluid)
    
    R     : radius of the ball (m)
    rho_b : density of the ball
    rho   : density of the air
    h     : initial height
    g     : acceleration
    """
    return 1 / np.sqrt(get_alpha(R, rho_b, rho, h, g))
