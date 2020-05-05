from vpython import *


scene.background = color.white
scene.width = 600
scene.height = 600
scene.forward = vector(-.5, -.3, -1)

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

x_axis = cylinder(color=vector(1, 0, 0), pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.3)
x_lbl = label(pos=vector(11, 0, 0), text="x-axis", color=color.red, opacity=0, height=30, box=0)
y_axis = cylinder(color=color.green, pos=vector(0,0,0), axis=vector(0,10,0), radius=0.3)
y_lbl = label(pos=vector(0, 11, 0), text="y-axis", color=color.green, opacity=0, height=30, box=0)
z_axis = cylinder(color=color.blue, pos=vector(0, 0, 0), axis=vector(0, 0, 10), radius=0.3)
z_lbl = label(pos=vector(0, 0, 11), text="z-axis", color=color.blue, opacity=0, height=30, box=0)

birthday_axis = cylinder(color=color.yellow, pos=vector(0, 0, 0), axis=vector(4, 8, 11), radius=0.3)
birthday_lbl = label(pos=vector(5, 9, 12), text="birthday vector", color=color.yellow, opacity=0, height=30, box=0)
#day day month
