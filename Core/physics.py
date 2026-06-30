from dataclasses import dataclass
from Rocket.rocket import Rocket
from Rocket.rocket_state import RocketState
from Physics.Core.vector2 import Vector2
from Rocket.engine import Engine

@dataclass
class Physics:
    gravity: Vector2 = Vector2(0, -9.81)

    def compute_gravity_force(self, mass: float) -> Vector2:
        return mass * self.gravity
    
    def compute_thrust(self, rocket: Rocket) -> Vector2:
        return rocket.engine.current_thrust_vector()
    
    def net_force(self, rocket: Rocket, engine: Engine, dt: float):
            return self.compute_gravity_force(rocket.mass()) + self.compute_thrust(rocket)
    
    def step(self, rocket: Rocket, engine: Engine,  dt: float) -> None:
        # 2. compute mass
        mass = rocket.mass()

        # 3. force
        net_force = self.net_force(rocket, engine,  dt)

        # 4. physics
        rocket.acceleration = net_force / mass

        # 5. integration
        rocket.velocity = rocket.velocity + rocket.acceleration * dt
        if rocket.velocity.y <= 0 and rocket.position.y <= 0:
             rocket.position = Vector2(0, 0)
        else:
             rocket.position = rocket.position +  rocket.velocity * dt

#if __name__ == "__main__":
    #physics_test: Physics = Physics()
    #rocket_test: Rocket = Rocket()