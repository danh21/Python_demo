import math
class fraction_custom:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show (self):
        if (self.x>0 and self.y<0) or (self.x<0 and self.y>0):
            GCD = - math.gcd(self.x, self.y)
        else:
            GCD = math.gcd(int(self.x), int(self.y))
        self.x /= GCD
        self.y /= GCD
        if self.y == 1:
            return str("%d"%self.x)
        else:
            return str("%d"%self.x) + "/" + str("%d"%self.y)
    def add (self, other):
        denominator = math.lcm(int(self.y), int(other.y))
        tempSelfX = self.x * denominator/self.y
        tempOtherX = other.x * denominator/other.y
        numerator = tempSelfX + tempOtherX
        sum = fraction_custom(numerator, denominator)
        return sum
    def mul (self, other):
        product = fraction_custom(self.x * other.x, self.y * other.y)
        return product