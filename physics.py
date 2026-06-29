from dataclasses import dataclass
from rocket import Rocket

@dataclass
class Physics:
    gravity: float = -9.81

    def compute_gravity_force(self, mass: float):
        return mass * self.gravity
    
    def burn_fuel(self, rocket: Rocket, dt: float):
         if not rocket.engine_on:
            return
         
         rocket.fuel_mass -= rocket.fuel_burn_rate * dt

         if rocket.fuel_mass <= 0:
              rocket.fuel_mass = 0
              rocket.engine_on = False
              rocket.thrust = 0
    
    def net_force(self, rocket: Rocket, dt: float):
            return self.compute_gravity_force(rocket.get_mass()) + rocket.thrust
    
    def step(self, rocket: Rocket, dt: float) -> None:
        # 1. update fuel FIRST (state change)
        self.burn_fuel(rocket, dt)

        # 2. compute mass ONCE
        mass = rocket.get_mass()

        # 3. forces
        gravity_force = self.compute_gravity_force(mass)
        thrust_force = rocket.thrust if rocket.engine_on else 0.0
        net_force = gravity_force + thrust_force

        # 4. physics
        acceleration = net_force / mass

        # 5. integration
        rocket.velocity += acceleration * dt
        if rocket.velocity <= 0 and rocket.position <= 0:
             rocket.position = 0
        else:
             rocket.position += rocket.velocity * dt

if __name__ == "__main__":
    physics_test: Physics = Physics()
    rocket_test: Rocket = Rocket()
    print(physics_test.net_force(rocket=rocket_test, dt=0.1))
    print(rocket_test.get_mass())
    print(rocket_test.engine_on)
    print(rocket_test.thrust)
    print(physics_test.compute_gravity_force(rocket_test.get_mass()))