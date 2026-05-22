

# print(ord("A"))
# print(ord("a"))

# # Question -
# a= input("give me a character : - ")
# value = ord(a)
# if value >= 65 and value <= 90:
#     print("it is an alphabet")
# elif value >= 97 and value <= 122:
#     print("its an albhabet")
# else:
#     print("not an albhabet")


# #Topic - For loop and while loop
# #For loop work on range but while loop work on condition example bucket and mugs

# for i in range(1,11 ,1):
#     print(i)

# for i in range(50 ,151 ,1):
#     print(i)

# for i in range (20 ,31):
#     print(i)

# for i in range (-12 , 11,1):
#     print(i)

# for i in range (10 , -11, -1 ):
#  print(i)


     ##                 Date -- 6 april 2026



# print table
# for i in range (5 ,51 , 5):
#     print(i)

# for i in range (7, 71 ,7):
#     print(i)

# a = int(input("please tell me a number :")) 
# for i in range (a ,a*10+1 , a):
#     print(i)

# for i in range(100):
#     print("hello world")

# # print n natural number
  
# n = int(input("tell you stop point :"))
# for i in range (1, n+1 , 1):
#     print(i)

# reverse for loop
# n = int(input("please tell your number :"))
# for i in range(n ,0 ,-1):
#     print(i)


# print a table
# number = int(input("enter a number :"))
# for i in range(1 ,11,):
#      print(f"{number} x {i} = {number * i}")

# # Question) sum of two n terms
# n = int(input("enter a number :"))
# a = 0
# for i in range(1 ,n+1 ):
#     a = a + i
# print(a)

# Factorial of a number


# #                            Date -- 7april 2026


# Question -  Find factorial 

# n = int(input("enter a number :"))
# a = 1 
# for i in range(1 , n+1 ):
#     a = a * i
# print(a)


# Question ) print odd and even using for loop

# n = int(input("give me a number : "))
# evensum = 0
# oddsum = 0
# for i in range(1 , n+1 ):
#     if i % 2 == 0:
#         evensum = evensum + i
#     else:
#         oddsum = oddsum + i

# print(f"even sum is: {evensum} and odd sum is :{oddsum}")

 
# Question) find factor of a number

# n = int(input("which number factor you want : ")) 

# for i in range(1 , n+1 ):
#     if n % i == 0:
#         print(i)


 
# #.                    #  Date -- 8 April 2026


#.     TOPIC - special number 

# n = int(input("tell me your number :"))
# factsum = 0
# for i in range( 1,n):
#     if n % i == 0:
#         factsum = factsum + i

# if factsum == n:
#     print("your number is perfect")
# else:
#     print("number is not perfect")


         ##.     TOPIC NUMBER --   PRIME NUMBER

# n = int(input("tell me your number"))
# count = 0

# for i in range(1 , n+1):
#     if n % i == 0:
#         count = count + 1

# if count == 2:
#     print("my number is prime")

# else:
#     print(" my number is composite number ")

# or 

n = int(input("tell me your number :"))

for i in range (2 ,(n//2)+ 1):
    if n % i == 0:
        print("your number is not prime")
        break
else:
    print("your number is prime")




# #                      Date - 9-April-2026



# n = int(input("tell me your number :"))

# for i in range (2 ,(n//2)+ 1):
#     if n % i == 0:
#         print("your number is composite")
#         break
# else:
#     print("your number is prime")



# #      Topic - Armstrong number

# a = 123
# while a > 0:
#     print(a % 10)
#     a = a// 10
    


#.                       Date - 10 april 2026

# Topic -- sum of digit

# n = int(input("tell your number :"))
# sum = 0

# while n != 0:
#     sum = sum + n%10
#     n = n//10
# print(sum)


# Topic -     reverse a number

# n = int(input("tell your number :"))
# rev = 0

# while n != 0:
#     rev = rev * 10 + n % 10
#     n = n // 10

# print(rev)

 # Topic -- check palindrome 

# n = int(input("plese tell your number :"))
# copy = n
# rev = 0
# while n != 0:
#     rev = rev * 10 + n % 10
#     n = n // 10

# if rev == copy:
#     print("palindrome")
# else:
#     print("not a palindrome")


#                                Date - 11 april 2026


# Question ) Take a digit input from user and reverse it using for loop

# n = input(" enter your digit :")
# print (n[::-1])

# or using for loop reverse number
# n = input(" enter your digit :")

# digit = " "
# for i in str(n)[:: -1]:
#     digit = digit + i
# print(digit)

# # question) print hello world 

# print("hell world\n" * 5)
# # or 
# for i in range(1, 6):
#     print("hello world")


# Topic - Fibonacci series upto n terms

# n = int(input(" enter your series no : "))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     a, b = b , a+b

# print the largest digit in a number
0
# n = 4289
# largest = 0
# for i in str(n):
#     a = int(i)
#     if a > largest:
#         largest = a

# print(largest)


# Question 4) Guessing game (user guesses a number until)

# import random
# akshay = random.randint(1,50)   # yedi function ke aage "." lag jay to o method ban jata hai
# for i in range(5):
#     tanishq = int(input("enter your number :"))

#     if tanishq == akshay:
#         print("you won")
#         break
#     if tanishq < akshay:
#         print("too small go higher")
#     if tanishq > akshay:
#         print("too high values go for lower")
# else:
#         print(f"bhaiya harr agy. {akshay} no. hai")


# Question ) check wether a number is pallindrome

# num = 1221
# if str(num) == str(num)[:: -1]:
#      print(f"number {num} is palindrome")
# else:
#      print(f"number {num} is not palndrome")

# # question 6) keep taking input until enters 0,then print sum

# sum = 0
# while True:
#      n = int(input("enter your number :"))

#      if n == 0:
#           break
     
#      sum += n 
#      print(sum)


# Question ) reverse a number using while loop

# n = int(input("enter a number :"))
# rev = 0
# while n != 0:
#      ld = n% 10
#      rev = n * 10 + ld
#      n = n // 10
# print(rev)

# Armstrong number or not

# n = 153 
# copy = n
# length = len(str(n))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit** length
#     n = n // 10
# if copy == sum:
#     print("Armstrong number ")
# else:
#     print("not Armstrong number ")
    



 #                             #   DATE - 13 APRIL 2026



