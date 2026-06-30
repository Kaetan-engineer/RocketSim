from dataclasses import dataclass
from rocket import Rocket
from rocket_state import RocketState
from Core.vector2 import Vector2

@dataclass
class Engine:
    max_thrust: Vector2 = Vector2(1_000_000, 1_000_000)

    fuel_mass: float = 45_000
    fuel_burn_rate: float = 250

    throttle: float = 0.5

    enabled: bool = False

    def update(self, rocket: Rocket, dt: float) -> None:
        if not self.enabled:
            return
        
        if self.fuel_mass == 0:
            rocket.state = RocketState.COASTING
            return
        
        self.fuel_mass -= self.fuel_burn_rate * dt
    
    def current_thrust_vector(self) -> Vector2:
        if self.enabled:
            return self.max_thrust * self.throttle
        else:
            return Vector2(0, 0)
    
    def shutdown(self) -> None:
        self.enabled = False
    
    def ignite(self) -> None:
        self.enabled = True