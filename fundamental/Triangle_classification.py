a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral triangle")
elif a==b or a==c or b==c:
    print("Isosceles triangle")
elif a+b>c or a+c>b or b+c>a:
    print("Scalene triangle")