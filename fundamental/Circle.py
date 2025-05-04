def circumference(radius):
    return 2 * 3.14 * radius

def area(radius):
    return 3.14 * radius**2



radius = float(input("Enter the radius of the circle: "))

print ("The circumference of the circle:", circumference(radius))
print("The area of the circle:", area(radius))