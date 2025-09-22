# a="infy"
# b=20.127
# c=10
# print(a,b,c)
# print(a,b,c,sep=":")
# print(a,b,c,end=" ")
# print(a,b,c)
# print("b=%0.2f" %b)
# print("c=%8d" %c)
# print("c=%-8d" %c)


# num1=10
# num2=5 
# num3=0 
# num4=2 
# num5=10 
# result = (num1==num5) and ((num2-num4*num3) == (num2-num3))
# result_1 = not(num3>=num4) and (num5/num2 == num4)
# result_2 = (num2-num4*num3) <= ((num2-num4)*num3)
# result_3 = not(num5>num4) or (num4+num2)>num1
# result_4 = (num1==num5) and (not(num5/num2 == num1/num2))
# print(result,result_1,result_2,result_3,result_4)

# num1 = 4
# num2 = 2
# num3 = 3
# num4 = 8
# result = num1/num4-num3*num2+num4
# print(result)

# if num1 % 3 ==0 and num1 % 5==0:
#     print("Zoom")
# elif num1 % 3 ==0:
#     print("ZIP")
# elif num1 % 5 ==0:
#     print("Zap")
# else:
#     print("invalid")

# num = 10
# count = 1
# while count <= num:
#     print(count)
#     count +=1

# for i in range(1,11):
#     print(i)
# for number in 1,2,3,4,5:
#     print("count the number: ",number)

# for number in range(1,5):
#     print ("The current number is ",number)
# print("---------------------------")
# for number in range(1,7,2):
#     print ("The current number is ",number)
# print("---------------------------")
# for number in range(5,0,-1):
#     print ("The current number is ",number)

# number_of_passengers=5
# number_of_baggage=2
# security_check=True
# for passenger_count in range(1, number_of_passengers+1):
#     for baggage_count in range(1,number_of_baggage+1):
#         if(security_check==True):
#             print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
#         else:
#             print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")


# num = 123

# positive_num = abs(num)

# total = 0
# while positive_num > 0:
#     print("normal number:",positive_num)
#     modulo = positive_num % 10
#     print("Modulo value:",modulo)
#     total += modulo
#     print("sum of two spearated values:",total)
#     positive_num //=  10
#     # print(positive_num)
#     # print (total)

# # print(total)

# def sum_of_digits(n: int) -> int:
#     return sum(int(digit) for digit in str(abs(n)))
# print(sum_of_digits(123))

# for passenger in "A","A", "FC", "C", "FA", "SP", "A", "A":
#     if(passenger=="FC" or passenger=="FA"):
#         print("No check required")
#         continue
#     if(passenger=="SP"):
#         print("Declare emergency in the airport")
#         break
#     if(passenger=="A" or passenger=="C"):
#         print("Proceed with normal security check")
#     print("Check the person")
#     print("Check for cabin baggage")
# print()
# num=10
# count=0
# while(count <= num):
#     if(count%2 == 0):
#         pass
#     else:
#         print(count)
#     count+=1


# Write a Python program to check whether the given year is leap year or not.

# year = int(input("Enter the year: "))

# if (year % 4 ==0  and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# Write a Python program to find and display the maximum of three given numbers.

# x,y,z =map(int ,input("enter x y z values: ").split())

# if x > y and x > z:
#     print("x is greater", x)
# elif y > x and y > z:
#     print(" y is maximun number", y)
# elif x == y == z:
#     print("all numbers are equal") 
# else:
#     print("z is maximum number")


# x, y, z = map(int, input("Enter x y z values: ").split())

# max_value = max(x, y, z)

# if x == y == z:
#     print("All numbers are equal")
# elif max_value == x:
#     print("x is the maximum number:", x)
# elif max_value == y:
#     print("y is the maximum number:", y)
# else:
#     print("z is the maximum number:", z)

# def is_prime(n):
#     if n == 1:
#         print(f"{n} prime")
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print(f"{n} is not prime")
#         else:
#             print(f"{n} is prime")


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n/2) + 1):
#         if n % i == 0:
#             return False
#     return True
# check = is_prime(17)

# if check is False:
#     print("not a prime number")
# else:
#     print("its a prime number")

# Write a Python program to print first n Fibonacci numbers.

# def fibanocci(num):
#     num1,num2 = 0,1
#     for i in range(num):
#         print(num1,end =" ")
#         res = num1 + num2
#         num1 = num2
#         num2 = res

# fibanocci(10)

# job_level = 1

# if job_level == 5:
#     percentage = 5
#     print(f"you have {percentage}% hike")
# elif job_level == 3:
#     percentage = 15
#     print(f"you have {percentage}% hike")
# elif job_level == 4:
#     percentage = 7
#     print(f"you have {percentage}% hike")
# else:
#     percentage = 0
#     print(f"you have {percentage}% hike")


# num1=100
# num2=200
# num3=6
# if(5>=num3):
#     if(num1>100 or num2>150):
#         print("1")
# elif(num1>=100 and num2>150):
#     print("2")
# else:
#     print("3")
# num1 = 5
# num2 = 1
# if((num1/num2==5) and (num1+num2)>5):
#     print("1")
# elif((num1-num2)<=1 or (num1%num2)==0):
#     print("2")
# else:
#     print("3")

# a = -10
# b = -200
# c = 2000
# d = 4000
# if( a*b >=d):
#     if(d>c):
#         if(d%c!=0):
#             print(11)
#         else:
#             print(22)
# else:
#     if(b/a >0):
#         if(a<b or d%c!=0):
#           print(33)
#         else:
#           print(44)

# for number in 10,15:
#     for counter in range(1,3):
#         print(number*counter, end=" ")

# number=28
# for num in range(25,30):
#     if(number>num):
#         print(num)
#     else:
#         print(num)
#         break

# for num in 23, 45, 50, 65, 76, 90:
#     if(num%5!=0):
#         continue
#     if(num%10==0):
#         print(num, end=" ")
#         continue
#     if(num%3==0):
#         print(num, end=" ")

# num1=16
# num2=6
# while(num1>=2):
#     if(num1>num2):
#         num1=num1/2
#     else:
#         print(num1)
#         break

# observe1="What's happening!!"
# def passport_check(passport_no):
#     observe4="actual copied to formal"
#     observe5="func. execution starts"
#     if(len(passport_no)==8):
#         if(passport_no[0]>="A" and passport_no[0]<="Z"):
#             status="valid"
#         else:
#             status="invalid"
#     else:
#         status= "invalid"
#     observe6="func. execution ends"
#     return status
# observe2="function with formal arg."
# observe3="calling with actual arg."
# passport_status=passport_check("M9993471")
# print("Passport is",passport_status)




# Write a Python function, find_square() that accepts an integer number n and returns the square of n. Invoke the function and display the square of the number. 

# def find_square(num):
#     result =num**2
#     return result
    
# print(find_square(3))


# Write a Python function, find_sum() that accepts an integer n and returns the sum of first n numbers. Invoke the function and display the sum of first n numbers.

# def find_sum(num):
#     sum = 0
#     for i in range(num+1):
#         sum += i
#     return sum
# print(find_sum(10))