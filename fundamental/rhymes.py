"""
• Write a program that judges a couplet by giving it one point if it
    - is composed of two verses with lengths within 4 chars of each other,
    - "rhymes" (the two verses end with the same last two letters),
    - alliterates (the two verses begin with the same letter).
• A couplet which gets 2 or more points is "good"
    Example logs of execution:
    (run #1)
    First verse: I joined the CS party
    Second verse: Like "LN" and Marty
    2 points: Keep it up, lyrical genius!

    (run #2)
    First verse: And it's still about the Benjamins
    Second verse: Big faced hundreds and whatever other synonyms
    0 points: Aw, come on. You can do better...
"""

verse1 = input("First verse: ")
verse2 = input("Second verse: ")
point = 0
num1 = len(verse1)
num2 = len(verse2)
if (verse1[0] == verse2[0]):
    point += 1
while verse1[num1-2:num1] == verse2[num2-2:num2]:
    point += 1
    num1 -= 2
    num2 -= 2
if point >= 1:
    print (point, "points: Keep it up, lyrical genius!")
else:
    print (point, "points: Aw, come on. You can do better...")
