# def table_multple(num):
#     for i in range(1, 11):
#         print(i*num, end="\n")
#     print()
# table_multple(2)

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in range(len(numbers)):
#     if numbers[i]>500:
#         break
#     elif numbers[i]>150:
#         continue
#     elif numbers[i] % 5  == 0:
#         print(numbers[i])

# number = 7895456789
# count =0
# while(number !=0 ):
#     number = number // 10
#     count+=1
# print(count)

# rows = 6
# for i in range(rows,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

# n = 7
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print("new")

# list1 = [10, 20, 30, 40, 50]
# reverse list
# new_list = reversed(list1)
# # iterate reversed list
# for item in new_list:
#     print(item)
# size = len(list1)
# for i in list1[::-1]:
#     print(i)

# for i in range(-10,0,1):
#     print(i)
# else:
#     print("Done !")

count = 0
def is_prime_bw(start,end):
    for num in range(start,end+1):
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                count +=1
                print(int(num),count)
numbers = is_prime_bw(2,100)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# is_prime(numbers)
# def fibanocci(num):
#     num1,num2=0,1
#     for i in range(num):
#         print(num1,end=" ")
#         res = num1 + num2
#         num1 = num2
#         num2 = res

# fibanocci(10)

# def factorial(num):
#     factorial = 1
#     if num < 0:
#         print("Factorial does not exist for negative numbers")
#     elif num == 0:
#         print("The factorial of 0 is 1")
#     else:
#         for i in range(1, num + 1):
#             factorial = factorial * i
#         print("The factorial of", num, "is", factorial)

# factorial(5)
# def is_palindrome(num):
#     return str(num) == str(num)[::-1]

# def num_reverse(num):
#     digit = num
#     number = 0
#     while num > 0:
#        reminder  = num % 10
#        number = (number*10)+reminder
#        num = num //10
#     print(f'{digit} reversed number: {number}')
#     if is_prime(number):
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")
#     if is_palindrome(number):
#         print(f"{number} is a palindrome number")
#     else:
#         print(f"{number} is not a palindrome number")

# num_reverse(77977)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # stat from index 1 with step 2( means 1, 3, 5, an so on)
# for i in my_list[1::2]:
#     print(i, end=" ")

# def cube_number(num):
#     for i in range(1, num+1):
#         print(f"Current Number is : {i}  and the cube is {i**3}")

# cube_number(6)

# def sum_seq(num, terms):
#     sum_seq =0
#     for i in range(0, terms):
#         print( num ,end =" ")
#         sum_seq += num
#         num = num * 10 + 2
#     print("\nSum of above series is:",sum_seq)
# sum_seq(2,5)

# def triangle_pattern(num):
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             print("*", end= " ")
#         print('\r')
#     for i in range(num,0, -1):
#         for k in range(i-1):
#             print("*", end=" ")
#         print('\r')
# triangle_pattern(5)

# def multiplicaitions(num):
#     for i in range(1, num+1):
#         print('multiplication table of:', i)
#         for j in range(1, 11):
#             print(f" {i * j}", end="")
#         print()
# multiplicaitions(5)
# def print_alternate_pattern(rows):
#     num = 1
#     for i in range(1,rows+1):
#         if i % 2 != 0:
#             for x in range(num, num + i):
#                 print(x, end=' ')
#             print() 
#         else: 
#             for y in range(num + i - 1, num - 1, -1):
#                 print(y, end=' ')
#             print()
#         num += i
# print_alternate_pattern(5)
# import os
# if os.path.exists("mymodule.py"):
#   os.remove("mymodule.py")
# else:
#   print("The file does not exist")

# count = 0
# n = int(input("Enter a number:"))
# for i in range(1, n+1):
#      if n % i == 0:
#             count +=1
# if count == 2:
#      print(n, "is a Prime number")
# else:
#      print(n, "is Not a Prime number")