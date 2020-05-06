import vpython as vp

initial_position1 = vp.vector(-10, 5, 5)
initial_velocity1 = vp.vector(10, -7, 0)
ball1 = vp.sphere(pos=initial_position1, radius=0.1, color=vp.color.red, make_trail=True)
initial_position2 = vp.vector(-10, -5, 5)
initial_velocity2 = vp.vector(10, 5, 0)
ball2 = vp.sphere(pos=initial_position2, radius=0.1, color=vp.color.yellow, make_trail=True)


wall_center = vp.vector(0., 0., 0.)
wall_dimensions = vp.vector(0.25, 10., 10)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.005
stop_time = 2.

time = 0.
ball_velocity1 = initial_velocity1
ball_velocity2 = initial_velocity2
while time < stop_time:
    vp.rate(rate_of_animation)
    if (ball1.pos.x + .15) > wall.pos.x:
        ball_velocity1.x = -ball_velocity1.x  # reverse ball velocity
    ball1.pos.x += ball_velocity1.x * time_step
    ball1.pos.y += ball_velocity1.y * time_step
    ball1.pos.z += ball_velocity1.z * time_step
    if (ball2.pos.x + .15) > wall.pos.x:
        ball_velocity2.x = -ball_velocity2.x  # reverse ball velocity
    ball2.pos.x += ball_velocity2.x * time_step
    ball2.pos.y += ball_velocity2.y * time_step
    ball2.pos.z += ball_velocity2.z * time_step
    time += time_step