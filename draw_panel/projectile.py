from math import *
from drawingpanel import *
panel = DrawingPanel(800, 700)
g = 9.8
steps = 50
def projectile(v, o, color="black"):
    for t in range (steps):
        x = v * t * cos(radians(o))
        y = v * t * sin(radians(o)) - 1/2 * g * t**2
        panel.canvas.create_oval(x, 700-y, x+3, 700-(y+3), fill=color)
projectile(30, 85)
projectile(60, 85, "red")
projectile(120, 85, "green")