import vpython as vp

vp.scene.background = vp.color.black

initial_position1 = vp.vector(0, 2, 5)
initial_position2 = vp.vector(0, -10, 5)
initial_position3 = vp.vector(0, -23, 5)

earth = vp.sphere(pos=initial_position1, radius=0.5, color=vp.color.blue, make_trail= True)
mars = vp.sphere(pos=initial_position2, radius=0.5, color=vp.color.magenta, make_trail= True)
moon = vp.sphere(pos=initial_position3, radius=0.5, color=vp.color.white, make_trail= True)

earth_field = vp.box(pos=vp.vector(0., 7., 0.), size=vp.vector(0.2, 10., 10), color=vp.color.green)
mars_field = vp.box(pos=vp.vector(0., -5., 0.), size=vp.vector(0.2, 10., 10), color=vp.color.red)
moon_field = vp.box(pos=vp.vector(0., -18., 0.), size=vp.vector(0.2, 10., 10), color=vp.color.gray(0.5))

initial_velocity = vp.vector(10, -3, -1)
accel_earth = vp.vector(0, -9.8, 0)  # Gravity Earth
accel_mars = vp.vector(0, -3.7, 0)  # Gravity Mars
accel_moon = vp.vector(0, -1.6, 0)  # Gravity Moon

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.01
stop_time = 600

time = 0.


while time < stop_time:
    vp.rate(rate_of_animation)
    x = earth.pos.x + initial_velocity.x * time_step + 0.5*accel_earth * time_step**2
    y = earth.pos.y + initial_velocity.y * time_step + 0.5*accel_earth * time_step**2
    z = earth.pos.z + initial_velocity.z * time_step + 0.5*accel_earth * time_step**2
    earth.pos = vp.vector(x,y,z)
    x = mars.pos.x + initial_velocity.x * time_step + 0.5*accel_mars * time_step**2
    y = mars.pos.y + initial_velocity.y * time_step + 0.5*accel_mars * time_step**2
    z = mars.pos.z + initial_velocity.z * time_step + 0.5*accel_mars * time_step**2
    mars.pos = vp.vector(x,y,z)
    x = moon.pos.x + initial_velocity.x * time_step + 0.5*accel_moon * time_step**2
    y = moon.pos.y + initial_velocity.y * time_step + 0.5*accel_moon * time_step**2
    z = moon.pos.z + initial_velocity.z * time_step + 0.5*accel_moon * time_step**2
    moon.pos = vp.vector(x,y,z)
    time += time_step
