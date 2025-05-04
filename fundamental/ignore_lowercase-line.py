def remove_lowercase(file1, file2):
    out = open(file2, "w")
    for line in open (file1):
        #if ord(line[0]) < 97:
        if not line[0] in "abcdefghijklmnopqrstuvwxyz":
            out.write (line)
    out.close()

remove_lowercase("assets\\longestLine_test.txt", "assets\\removeLowercase_test.txt")
print (open("assets\\removeLowercase_test.txt").read())