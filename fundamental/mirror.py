size = 8
def mirror():
    print ("#" + size*2*"=" + "#")
    for i in range (size-2, -1, -2):
        print ("|" + i*" " + "<>" + (size-2-i)*2*"." + "<>" + i*" " + "|")
    for i in range (0, size, 2):
        print ("|" + i*" " + "<>" + (size-2-i)*2*"." + "<>" + i*" " + "|")
    print ("#" + size*2*"=" + "#")
mirror()