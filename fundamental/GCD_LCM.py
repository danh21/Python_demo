def LCM(a, b):
    if a == 0 or b == 0:
        return 0
    if a >= b:
        LCM = a
    else:
        LCM = b
    for i in range(a * b):
        if LCM % a == 0 and LCM % b == 0:
            return LCM
        LCM += 1
    return LCM

def GCD(a,b):
    if a == 0 or b == 0:
        return a + b
    return (a * b) / LCM(a, b)



a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("LCM(a,b) =", LCM(a,b))    
print("GCD(a,b) =", GCD(a,b))    