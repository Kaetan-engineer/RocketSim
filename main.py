from physics import Physics
from rocket import Rocket

rocket = Rocket()
physics = Physics()

dt = 0.1
time = 60

steps = int(time / dt)
t = 0.0

for _ in range(steps + 1):
    if t >= rocket.launch_time:
        rocket.engine_on = True
        
    physics.step(rocket, dt)

    print(
        f"t={t:.2f}s  "
        f"y={rocket.position:.2f}m  "
        f"vy={rocket.velocity:.2f}m/s"
    )

    t += dt