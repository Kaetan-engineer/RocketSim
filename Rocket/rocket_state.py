from __future__ import annotations
from enum import Enum, auto

class RocketState(Enum):
    PRELAUNCH = auto()
    COUNTDOWN = auto()
    IGNITION = auto()
    ASCENT = auto()
    COASTING = auto()
    LANDED = auto()
    ABORTED = auto()


    def is_engine_active(self) -> bool: 
        return self in ( 
            RocketState.IGNITION, 
            RocketState.ASCENT
        )

    def is_in_flight(self) -> bool: 
        return self in ( 
                RocketState.IGNITION, 
                RocketState.ASCENT, 
                RocketState.COASTING 
            )

    def is_terminal(self) -> bool: 
        return self in ( 
                RocketState.LANDED, 
                RocketState.ABORTED 
            )
    
    def produces_thrust(self) -> bool:
        return self in (
            RocketState.IGNITION,
            RocketState.ASCENT
        )
    
    def can_transition_to(self, other: RocketState) -> bool:
        TRANSITONS = {
            RocketState.PRELAUNCH: [RocketState.COUNTDOWN],
            RocketState.COUNTDOWN: [RocketState.IGNITION],
            RocketState.IGNITION: [RocketState.ASCENT],
            RocketState.ASCENT: [RocketState.COASTING, RocketState.ABORTED],
            RocketState.COASTING: [RocketState.LANDED, RocketState.ABORTED]
        }

        return other in TRANSITONS[self]

    def next_state(self) -> RocketState:
        NEXT_STAGE = {
            RocketState.PRELAUNCH: RocketState.COUNTDOWN,
            RocketState.COUNTDOWN: RocketState.IGNITION,
            RocketState.IGNITION: RocketState.ASCENT,
            RocketState.ASCENT: RocketState.COASTING,
            RocketState.COASTING: RocketState.LANDED
        }
        return NEXT_STAGE[self]

    def can_abort(self) -> bool:
        return self in (
          RocketState.COUNTDOWN,
          RocketState.IGNITION,
          RocketState.ASCENT,
          RocketState.COASTING
        )

    def is_launch_sequence(self) -> bool
        pass