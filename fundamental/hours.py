sum = 0
days = 0
count = 0
for line in open ("assets\hours.txt"):
    token = line.split()
    for i in range (2, len(token)):
        sum += float(token[i])
        days += 1
    avr = sum/days
    for i in range (2, len(token)):
        if float(token[i]) > avr:
            count += 1
    print (token[1], "worked", "%.1f"%sum, "hours,", "%.2f"%(avr), "/ day,", count, "days above average")
    sum = 0
    days = 0
    count = 0