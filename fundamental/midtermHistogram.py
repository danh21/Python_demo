count = 0
cnt = 0
dem = 0
num = []
for line in open ("assets\midtermScores.txt"):
    num.append(line.strip())
for i in range (len(num)-1):    #sap xep tu be den lon
    for j in range (i+1, len(num)):
        if num[i] > num[j]:
            temp = num[j]
            num[j] = num[i]
            num[i] = temp
for score in num:
    dem += 1
    for score1 in num: #dem so lan lap
        if score == score1:
            count += 1
    for i in range (dem):   #tranh lap lai khi xuat
        if score == num[i]:
            cnt += 1
    if cnt == 1:
        print (score + ": " + count*"*")
    cnt = 0
    count = 0