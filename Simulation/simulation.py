from dataclasses import dataclass
from Rocket.rocket import Rocket
from Rocket.rocket_state import RocketState

@dataclass
class Simulation:
    def update_state(self, rocket: Rocket, dt: float):
        pass