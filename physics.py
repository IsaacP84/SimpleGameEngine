import numpy as np

from globals import FRICTION_COEFFICIENT

def normalize(f):
    magnitude = np.linalg.norm(f)
    if(magnitude <= 0.001):
        return (0,0,0)
    return f / magnitude

def applyFriction(e, coeffient):
    # r, theta, phi = cartesian_to_spherical(e.vel[0], e.vel[1], e.vel[2])
    # ideally get the angle of whatever the entity is touching/standing on
    # im gonna assume flat plane along the xy axis, so z value doesn't really matter
    
    magnitude = np.linalg.norm(e.vel)
    if(magnitude <= 0.01):
        return
    unit_vec3 = e.vel / magnitude
    
    weight = e.weight if hasattr(e, "weight") else 1
    f_mag = coeffient * weight
    if f_mag > magnitude:
        f_mag = magnitude
    f = unit_vec3 * -1 * f_mag
    
    # print(f"Vel: {e.vel}")
    # print(f"Friction vector: {f}")
    
    e.applyForce(f)
    return



def cartesian_to_spherical(x, y, z):
    """
    Converts 3D Cartesian coordinates to spherical coordinates.

    Args:
        x (float or np.ndarray): The x-coordinate(s).
        y (float or np.ndarray): The y-coordinate(s).
        z (float or np.ndarray): The z-coordinate(s).

    Returns:
        tuple: A tuple containing the spherical coordinates (r, theta, phi).
               r: Radial distance (radius).
               theta: Polar angle (inclination) from the positive z-axis.
               phi: Azimuthal angle (rotation) in the xy-plane from the positive x-axis.
    """
    r = np.sqrt(x**2 + y**2 + z**2)
    # Handle the case where r is 0 to avoid division by zero
    theta = np.arccos(z / r) if r != 0 else np.zeros_like(x)
    phi = np.arctan2(y, x)
    return r, theta, phi

    
def physics(entities):
    for e in entities:
        applyFriction(e, FRICTION_COEFFICIENT)
        
    for e in entities:
        for i in range(3):
            e.pos[i] += e.vel[i]
            
        magnitude = np.linalg.norm(e.vel)
        if(magnitude <= 0.01):
            e.vel *= 0
            
    for e in entities:
        e.update()
        
    return