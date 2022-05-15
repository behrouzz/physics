# https://www.deboecksuperieur.com/site/328907
import numpy as np

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

R = 0.01       # rayon de la bille en mètres
rho_b = 1000.  # masse volumique de la bille
rho = 1.2      # masse volumique de l'air
g = 9.81       # accélération de la pesanteur
h = 100        # hauteur initiale

alpha = get_alpha(R, rho_b, rho, h, g=9.81)

vlim = 1 / alpha**0.5
