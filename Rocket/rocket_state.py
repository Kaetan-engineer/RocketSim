from enum import Enum, auto
from rocket import Rocket

class RocketState(Enum):
    PRELAUNCH = auto()
    COUNTDOWN = auto()
    IGNITION = auto()
    ASCENT = auto()
    COASTING = auto()
    LANDED = auto()
    ABORTED = auto()

    def is_engine_active(self) -> bool:
        return self in (RocketState.IGNITION, RocketState.ASCENT)
    
    def is_in_flight(self) -> bool:
        return self in (self.IGNITION, self.ASCENT, self.COASTING)
    
    def is_terminal(self) -> bool:
        return self in (RocketState.LANDED, RocketState.ABORTED)