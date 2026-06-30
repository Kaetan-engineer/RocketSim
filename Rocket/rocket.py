from Core.vector2 import Vector2
from dataclasses import dataclass
from rocket_state import RocketState
from engine import Engine


@dataclass
class Rocket:
    position: Vector2 = Vector2(0, 0)
    velocity: Vector2 = Vector2(0, 0)
    acceleration: Vector2 = Vector2(0, 0)

    dry_mass: float = 5_000

    engine: Engine = Engine()

    state: RocketState = RocketState.PRELAUNCH

    def mass(self) -> float:
        return self.dry_mass + self.engine.fuel_mass