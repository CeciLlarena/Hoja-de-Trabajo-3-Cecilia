def linearsearch(arr, n, x):
    for i in range (0,n):
        if (arr[i] == x):
            return i
    return -1

arr = [8,9,10,11]

x = 1
n= len(arr)
position = linearsearch(arr, n, x)
if (position == -1):
    print ("element not foud")
else:
    print("element is present at index", position)