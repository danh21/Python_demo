# Example while loop (prime number).
i = 2

while (i < 100):
    j = 2

    while (j <= (i/j)): # nested
        if not (i % j): break 
        j = j + 1

    if (j > i/j): print("{} is prime".format(i))

    i = i + 1
else:
    print("Else of while!")

print("End!")

