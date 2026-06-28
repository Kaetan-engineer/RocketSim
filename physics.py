from vector3 import Vector3
from rocket import Rocket

GRAVITY = 9.81

def gravity_force(rocket: Rocket):

    return Vector3(
        0,
        0,
        -rocket.propellant_mass * GRAVITY
    )

def thrust_force(rocket: Rocket):

    if not rocket.has_fuel:
        return Vector3()
    
    return Vector3(
        0,
        0,
        rocket.thrust
    )

def compute_forces(rocket: Rocket):

    rocket.reset_forces()

    rocket.add_force(
        gravity_force(rocket)
    )

    rocket.add_force(
        thrust_force(rocket)
    )