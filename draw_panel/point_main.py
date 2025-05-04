from point import *
from drawingpanel import *
panel = DrawingPanel(400, 300)
p = Point(3, -14)
p1 = Point(20, 30)
#print (p.x, p.y)
#print (p)
print ("The point is " + str(p) + "!")

Point.translate(p,1,2)
print ("The point is " + str(p) + "!")

print(Point.distance_from_origin(p))

Point.draw(p1, panel, "red")