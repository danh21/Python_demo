# region API
def length(string):
    len = 0
    for i in string:
        len += 1
    return len

def rotation(string, times):
    length = len(string)
    for i in range (0, length):
        if string[i] == ' ':
            print(" ", end="")
        else:
            print(chr(ord(string[i])+times), end="")

def isVowel(string):
    if string[0] in "aeiouAEIOU":
        return 1
    return 0

def LengthGreaterThan3(string):
    str_temp = []
    string = string.split(" ")
    for i in string:
        if len(i) > 3:
            str_temp.append(i)
    return str_temp

def reverse(string):
    lst = string.split(" ")
    new_lst = []
    for i in range (len(lst)-1, -1, -1):
        new_lst.append(lst[i])
    print (" ".join(new_lst))
# endregion



str = input("Enter the string: ")

print("Length of string:", length(str))

times = 1
print("String after rotating", times, "times: ", end="")
rotation(str, times)

if isVowel(str):
    print ("\nString starts with a vowel!")
else:
    print ("\nString starts with a consonant!")

print("Sub strings whose length is greater than 3", LengthGreaterThan3(str))

print("Reverse string:", end=" ")
reverse(str)