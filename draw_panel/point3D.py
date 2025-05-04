from point import *
class Point3D(Point):
    z = 0
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z
    def translate(self, dx, dy, dz):
        Point.translate(self, dx, dy)
        self.z += dz