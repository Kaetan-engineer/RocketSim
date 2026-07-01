from dataclasses import dataclass
from rocket_state import RocketState
from Core.vector2 import Vector2
from math import cos, sin

@dataclass
class Engine:
    max_thrust: float = 1_000_000

    fuel_mass: float = 45_000
    fuel_burn_rate: float = 250

    throttle: float = 0.5

    enabled: bool = False

    @property
    def orientation(self) -> Vector2:
        return Vector2(
            cos(self.angle), sin(self.angle)
        )
    
    def rotate_left(self, dt):
        self.angle -= 1 * dt
    
    def rotate_right(self, dt):
        self.angle += 1 * dt

    def update(self, dt: float) -> None:
        if not self.enabled:
            return
        
        fuel_used = self.fuel_burn_rate * dt
        self.fuel_mass = max(0.0, self.fuel_mass - fuel_used)

        if self.fuel_mass == 0:
            self.shutdown()
        
    def thrust_magnitude(self) -> float:
        if not self.enabled:
            return 0.0
        
        if self.fuel_mass <= 0:
            return 0.0
        
        return self.max_thrust * self.throttle

    def current_thrust_vector(self, direction: Vector2) -> Vector2:
        magnitude = self.thrust_magnitude()

        if magnitude == 0:
            return Vector2(0, 0)
        
        return direction.normalized() * magnitude

    def shutdown(self) -> None:
        self.enabled = False
        
    
    def ignite(self) -> None:
        self.enabled = True