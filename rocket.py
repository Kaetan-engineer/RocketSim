from dataclasses import dataclass, field
from math import sqrt, log, radians, sin, cos
from vector3 import Vector3
    
@dataclass
class Rocket:
    #Transitional Motion
    position: Vector3 = field(default_factory=Vector3)
    velocity: Vector3 = field(default_factory=Vector3)
    acceleration: Vector3 = field(default_factory=Vector3)

    #Rotational Motion
    angle: float = 0.0                  #radians
    angular_velocity: float = 0.0       #rad/s
    angular_acceleration: float = 0.0   #rad/s^2

    torque: float = 0.0                 #N*m
    moment_of_inertia: float = 2.4e6

    #Forces
    net_force: Vector3 = field(default_factory=Vector3)

    #Mass
    dry_mass: float = 50_000            #kg
    propellant_mass: float = 450_000    #kg

    #Engine
    thrust: float = 8_000_000           #Newton
    exhaust_velocity: float = 3_500     #m/s
    mass_flow_rate: float = 250         #Kg/s

    #Simulation
    time:float = 0.0                    #seconds

    @property
    def total_mass(self):
        return self.dry_mass + self.propellant_mass
    
    @property
    def speed(self):
        return self.velocity.magnitude
    
    @property
    def altitude(self):
        return self.position.z
    
    @property
    def fuel_remaining(self):
        return self.propellant_mass
    
    @property
    def has_fuel(self):
        return self.propellant_mass > 0
    
    @property
    def delat_v_remaining(self):
        if not self.has_fuel:
            return 0.0
        
        return (
            self.exhaust_velocity *
            log(self.total_mass / self.dry_mass)
        )
    
    def burn_fuel(self, dt):
        burned = self.mass_flow_rate * dt
        self.propellant_mass = max(
            0.0,
            self.propellant_mass - burned
        )
    
    def compute_transitional_acceleration(self):
        self.acceleration = (
            self.net_force / 
            self.total_mass
        )

    def computate_angular_acceleration(self):

        self.angular_acceleration = (
            self.torque /
            self.moment_of_inertia
        )
    
    def intergrate(self, dt):
        #Semi-Implicit Euler

        #Linear Motion
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

        #Rotational Motion
        self.angular_velocity += (
            self.angular_acceleration * dt
        )
        self.angle += (
            self.angular_velocity * dt
        )

        self.time += dt
    
    def reset_forces(self):
        self.net_force = Vector3()

    def add_force(self, force):
        self.net_force += force

Falcon_9 = Rocket()