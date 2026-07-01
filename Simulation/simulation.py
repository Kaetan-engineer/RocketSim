from dataclasses import dataclass
from Rocket.rocket import Rocket
from Rocket.rocket_state import RocketState
from Core.physics import Physics

@dataclass
class Simulation:
    rocket: Rocket = Rocket()
    physics: Physics = Physics()
    dt: float = 0.1
    current_time: float = 0
    total_time: float = 30

    @property
    def step_count(self):
        return self.total_time / self.dt
    
    def step(self):
        self.rocket.engine.update(self.dt)
        self.physics.physics_step(self.rocket, self.rocket.engine, self.dt)

        self.total_time += self.dt
        self.print_status()
    
    def run(self):
        while self.current_time < self.total_time:
            self.step()
    
    def reset(self):
        pass

    def print_status(self):
        print(
            f"Time: {self.current_time:.2f}s  |  "
            f"Position; {self.rocket.position:.2f}  |  "
            f"Velocity: {self.rocket.velocity:.2f}  |  "
            f"Mass: {self.rocket.mass:.2f}kg  |  "
            f"State: {self.rocket.state}  |  "
        )