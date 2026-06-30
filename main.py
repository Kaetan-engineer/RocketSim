from Physics.Core.physics import Physics
from Rocket.rocket import Rocket
from Rocket.rocket_state import RocketState
from Rocket.engine import Engine

rocket = Rocket()
physics = Physics()
engine = Engine()

dt = 0.1
launch_time = 5.0
total_simulation_time = 60
current_simulation_time = 0.00

while current_simulation_time < total_simulation_time:
    if current_simulation_time >= launch_time:
        rocket.state = RocketState.COUNTDOWN
        
    physics.step(rocket, engine, dt)

    print(
        f"t={current_simulation_time:.2f}s  "
        f"y={rocket.position:.2f}m  "
        f"vy={rocket.velocity:.2f}m/s"
    )

    current_simulation_time += dt