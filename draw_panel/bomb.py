from point import *
from drawingpanel import *

X = int(input("Blast site x? "))
Y = int(input("Blast site y? "))
R = int(input("Blast radius? "))

panel = DrawingPanel(400, 300)
O = Point(X, Y)
a = Point(50, 20)
b = Point(10, 72)
c = Point(90, 60)
d = Point(74, 98)
e = Point(150, 91)
f = Point(5, 136)

panel.canvas.create_oval(X - R, Y - R, X + R, Y + R, outline="red")

for i in (a, b, c, d, e, f):
    d = Point.distance(i, O)
    if d < R:
        Point.draw(i, panel, color="red")
    else:
        Point.draw(i, panel, color="black")