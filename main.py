from dataclasses import dataclass

@dataclass
class Rocket:
    position: float = 0.0
    velocity: float = 0.0
    acceleration: float = 0.0

    dry_mass: float = 10_000
    propellant_mass: float = 90_000

    thrust: float = 0
    GRAVITY = -9.81

    exhaust_velocity: float = 1_000
    mass_flow_rate: float = 250

    time: float = 0.0

    @property
    def total_mass(self):
        if self.propellant_mass <= 0:
            return self.dry_mass
        return self.dry_mass + self.propellant_mass
    
    def compute_thrust(self):
        if self.propellant_mass <= 0:
            self.thrust = 0
            return
        
        self.thrust = self.mass_flow_rate * self.exhaust_velocity
    
    def comput_net_force(self):
        return self.GRAVITY + self.thrust
    
    def weight(self, mass: float):
        return self.GRAVITY * mass
    
    def fuel_remaining(self, dt):
        if self.propellant_mass == 0:
            return
        self.propellant_mass -= self.mass_flow_rate * dt

    def integrate(self, dt):
        self.acceleration = self.comput_net_force() / self.total_mass

        self.velocity += self.acceleration * dt

        self.position += self.velocity * dt

        self.time += dt

Falcon9 = Rocket()

simulation_time = 500
dt = 1

steps = int(simulation_time / dt)

for step in range(steps):

    Falcon9.compute_thrust()

    Falcon9.integrate(dt)

    Falcon9.fuel_remaining(dt)

    print(
        f"Time: {Falcon9.time:.2f}s  |  "
        f"Altitude: {Falcon9.position:.2f} m  |  "
        f"Velocity: {Falcon9.velocity:.2f} m/s  |  "
        f"Mass: {Falcon9.total_mass:.2f} kg  |  "
        f"Thrust: {Falcon9.thrust}"
    )