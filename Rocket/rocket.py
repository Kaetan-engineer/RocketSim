from Core.vector2 import Vector2
from dataclasses import dataclass
from rocket_state import RocketState
from engine import Engine
from math import pi


@dataclass
class Rocket:
    position: Vector2 = Vector2(0, 0)
    velocity: Vector2 = Vector2(0, 0)
    acceleration: Vector2 = Vector2(0, 0)

    dry_mass: float = 5_000

    engine: Engine = Engine()
    angle: float = pi

    state: RocketState = RocketState.PRELAUNCH

    @property
    def mass(self) -> float:
        return self.dry_mass + self.engine.fuel_mass
    
    def update_state(self, current_time: float) -> None:
        pass