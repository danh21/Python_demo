from random import *
count = 0
def roll():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return (dice1+dice2)

for i in (6,8,11,2,7):
    dice = roll()
    print (dice)
    if dice == i:
        count += 1

print ("You won", count, "after 5 tries!")