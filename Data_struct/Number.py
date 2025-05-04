# region API
def isEven(n):
    if (n % 2 == 0):
        return True
    else:
        return False

def isAbundant(n):
    if sumOfDivisors(n) > n:
        return True
    else:
        return False

def isPrime(n):
    if n <= 1:
        return False
    count = 0
    for i in range (2, n):
        if n % i == 0:
            count += 1 
    if count == 0:
        return True
    else:
        return False 

def isPowerOfFour (n):  # luỹ thừa của 4
    while n > 4:
        n = n / 4
    if n == 4:
        return True
    else:
        return False

def factorial(n):
    fac = n
    for i in range (n-1, 1, -1):
        fac *= i
    return fac

def factorsOfNum(n):
    for i in range (1, n+1):
        if n % i == 0:
            print(i)

def sumOfDivisors(n):
    sum = 0
    for i in range (1, n):
        if n % i == 0:
            sum += i
    return sum
# endregion
 

# region APP
num = int(input("Enter the number: "))

if isEven(num):
    print(num, "is even")
else:
    print(num, "is odd")
    
print(num, "is an abundant number ?", isAbundant(num))
print(num, "is an prime number ?", isPrime(num))

print("Factors of number:")
factorsOfNum(num)

print("Factorial of", num, ":", factorial(num))
# endregion