from math import *

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    if b == 0:
        print ("The equation has no root")
    else:
        x = -c/b
        print ("The equation has 1 root: x = ", x)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print ("The equation has no root")
    elif delta == 0:
        x = -b/(2*a)
        print ("The equation has roots: x1 = x2 = ", x)
    else:
        x1 = (-b + sqrt(delta)) / (2*a)           
        x2 = (-b - sqrt(delta)) / (2*a) 
        print("The equation has 2 roots: x1 =", x1, "; x2 =", x2)