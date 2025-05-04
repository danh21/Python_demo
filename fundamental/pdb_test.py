import pdb

gpa = int(input("What is your GPA? "))

pdb.set_trace()

if gpa > 3.5:
    print ("You have qualified for the honor roll.")
elif gpa > 2.0:
    print ("Welcome to Mars University!")
else:
    print ("Your application is denied.")