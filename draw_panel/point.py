from math import *
class Point:
    x = 0
    y = 0
    #def set_location(self, x, y):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, panel, color):
        panel.canvas.create_oval(self.x, self.y, self.x + 3, self.y + 3, fill=color)
        panel.canvas.create_text(self.x, self.y, text=str(self), anchor="sw", fill=color)

    def distance_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"