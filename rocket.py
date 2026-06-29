import time

class Rocket:
    def __init__(self) -> None:
        self.position: float = 0.0
        self.velocity: float = 0.0

        self.dry_mass: float = 5_000
        self.fuel_mass: float = 45_000
        self.fuel_burn_rate: float = 250  # kg per second

        self.thrust: float = 1_000_000
        self.engine_on: bool = False
        self.launch_time: float = 5.0

    def get_mass(self) -> float:
        return self.dry_mass + self.fuel_mass