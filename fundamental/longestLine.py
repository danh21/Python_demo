def input_stats (f):
    max = 0
    for line in open (f):
        if len(line) > max:
            max = len(line)
            s = line
    print ("longest line =", max, "characters")
    print (s)
input_stats ("assets\longestLine_test.txt")   