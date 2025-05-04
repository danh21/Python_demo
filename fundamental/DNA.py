count = 0
f = open("assets\\DNA.txt")
a = f.read()
length = len(a)
for n in range (0, length):
    if (a[n]=='C' or a[n]=='G'):
        count = count + 1
percent = count * 100 / length
print ("The percent of C+G present in the DNA:", percent, "%")