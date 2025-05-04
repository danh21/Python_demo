# region APIs
def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

def sortOdd(arr):
    newArr = []
    for i in arr:
        if i % 2 != 0:
            newArr.append(i)
    return newArr

def sortEven(arr):
    newArr = []
    for i in arr:
        if i % 2 == 0:
            newArr.append(i)
    return newArr

def sortUnique(arr):
    arr_temp = []
    flag = 0
    for i in arr:
        for j in arr_temp:
            if i == j:
                flag += 1
        if flag == 0:
            arr_temp.append(i)
        else: 
            flag = 0
    return arr_temp

def isSortedArray (arr):
    count = 0
    length = len(arr)
    for i in range (0, length-1):
        if arr[i] > arr[i+1]:
            count = count + 1
    if count == 0:
        return True
    else:
        return False
# endregion


# region MAIN
print("Enter the size of the array: ")
n = int(input())

# init array
lst = []
print("Enter the elements of the array: ")
for i in range(n):
    lst.append(int(input()))



# max element of array
print("Max =", max(lst))

# min element of array
print("Min =", min(lst))

# sum
print("Sum =", sum(lst))



print ("Array", lst, "is sorted ?", isSortedArray(lst))

# ascending order of elements
lst.sort()
print("Ascending order of elements:", lst)



# odd element of array
oddLst = sortOdd(lst)
print("Odd elements of array:", oddLst)

# even element of array
evenLst = sortEven(lst)
print("Even elements of array:", evenLst)

# unique element of array
uniqueLst = sortUnique(lst)
print("unique elements of array:", uniqueLst)
# endregion