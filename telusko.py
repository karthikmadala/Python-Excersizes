from array import *

arr = array('i',[])

n = int(input("enter the length of the array: "))

for i in range(n):
    x = int(input("enter the value: "))
    arr.append(x)
print(arr)

val = int(input("Enter the value for search: "))

for e in arr:
    if e == val:
        print(arr.index(e))
        break