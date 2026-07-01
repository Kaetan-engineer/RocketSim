from dataclasses import dataclass
from Rocket.rocket import Rocket
from Rocket.rocket_state import RocketState
from Physics.Core.vector2 import Vector2
from Rocket.engine import Engine
import math

@dataclass
class Physics:
    gravity: Vector2 = Vector2(0, -9.81)
    drag_coeffifient: float = 0.0005
    rocket_area: float = 10.5
    rho0: float = 1.225
    scale_height: float = 8500

    def compute_gravity_force(self, mass: float) -> Vector2:
        return mass * self.gravity
    
    def compute_thrust(self, rocket: Rocket) -> Vector2:
        return rocket.engine.current_thrust_vector()
    
    def air_density(self, altitude: float) -> float:
        altitude = max(0.0, altitude)

        return self.rho0 * math.exp(-altitude / self.scale_height)
    
    def compute_drag(self, velocity: Vector2, altitude: float) -> Vector2:
        V = velocity.magnitude
        if V == 0:
            return Vector2(0, 0)
        C = self.drag_coeffifient
        A = 10.75
        P = self.air_density(altitude)

        return Vector2(0, -0.5 * C * P * A * V**2)
    
    def net_force(self, rocket: Rocket, engine: Engine, dt: float):
            return (
                self.compute_gravity_force(rocket.mass) + 
                self.compute_thrust(rocket) +
                self.compute_drag(rocket.velocity, rocket.position.y)
            )
    
    def physics_step(self, rocket: Rocket, engine: Engine,  dt: float) -> None:
        # 2. compute mass
        mass = rocket.mass

        # 3. force
        net_force = self.net_force(rocket, engine,  dt)

        # 4. physics
        rocket.acceleration = net_force / mass

        # 5. integration
        rocket.velocity = rocket.velocity + rocket.acceleration * dt
        if rocket.position > 0:
            rocket.position = Vector2(0, 0)
        rocket.position = rocket.position +  rocket.velocity * dt

#if __name__ == "__main__":
    #physics_test: Physics = Physics()
    #rocket_test: Rocket = Rocket()