#.                       DATE -- 13 April 2026

# Topic --- function 
# function are block of reusuable code 

# two type-- 1. in-build function 2. userdefine fuction
# in-build function - print(), input(),len() etc.














#  parameter and  arguments 

# def addition(a,b): # a and b are parameters
#     print(a+b)

# addition(10,20)  # this is called argument when calling function

# check number is palindrome using function

# def palindrome(n):
#     rev = 0
#     copy = n
#     while n != 0:
#         rev = rev * 10 + n%10
#         n = n // 10

#     if copy == rev:
#         print("palindrome")
#     else:
#         print("not palindrome")

# palindrome(121)
# palindrome(134)
# palindrome(198891)
# palindrome(451)



# Type of argument
# 1) Positional arguments
# def multiply (a,b): #fixed position
#     print(a*b)

# multiply(12,67) # fixed arguments


# 2) Default arguments/ keyword
# def info(a,b,c,d,e):
#     print(a,b,c,d,e)

# info(12,34,e =67,c=12,d= 67)


# if you give a value using default argument you always have to give further using default arguments.

# defaut parameters
# def info(name , age, id = None):
#    print("info recieved")
# info("abhishek" ,24)


#.                          DATE -- 14 APRIL 2026


# def strongnumber():



# topic -- 

# def agechecker(n):
#     if n >= 18:
#         return True
#     else:
#         return False
    
# age = int(input("tell your age : "))

# if agechecker(age):
#     print("you can vote")
# else:
#     print("you can not vote"



#.    print 1 to 100 using function
# def numbers(n):
#     if n == 101:
#         return "done"
#     print(n)
#     numbers(n+1)
# numbers(1)

# # back tracking
# def numbers(n):
#     if n == 101:
#         return "done"
#     numbers(n+1)
#     print(n)
# numbers(1)


# Data structure 
#1) list
# 2) tuble
#3) set
# 4) dictionary



#                         DATE -- 15 APRIL, 2026


# reverse the string
# s = "shery"
# print(f" reverse string  : {s[::-1]}")
# print(f"length of string -> {len(s)}")
# print(f"string in upper format -> {s.upper()}")
# print(f"string in lower format -> {s.lower()}")

# Question 32) 

# s = "ShEry"
# lower = ""
# upper = ""
# for i in s:
#     if i.islower():
#         lower = lower + i
#     elif i .isupper():
#         upper = upper + i

# print(lower + upper)

# Question 33) Count all letters, digits, and special symbols from a given string

# str1 = "P@#yn26at^&i5ve"
# alpha = 0
# digit = 0
# special = 0
# for i in str1:
#     if i.isalpha():
#         alpha = alpha + 1
#     elif i.isdigit():
#         digit = digit + 1
#     else:
#         special = special + 1

# print(f"alphabet count : {alpha}")
# print(f"digit count : {digit}")
# print(f"special count : {special}")

# 34) Compare two strings without using inbuilt functionsx

# str1 = "hello"
# str2 = "Hello"
# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         if str[i] != str[2]:
#             print("string are not same")
#             break
#     else:
#         print("string are same")
# else:
#     print("both string  are of not the same length")




#.                            DATE --- 16 APRIL,2026

#questiion 35) find vowel 

# str1 = "Hello"
# vowels = "aeiouAEIOU"
# count = 0

# for i in str1:
#     if i in vowels:
#         count += 1
# print(f"total count of vowel are: {count}")

#  or.  by function find vowels

# def countvowels():
#     str1 = "Hello"
#     vowels = "aeiouAEIOU"
#     count = 0

#     for i in str1:
#         if i in vowels:
#             count += 1
#             print(i)
#     return f"total count of vowel are : {count}"
# print(countvowels())


# Question 36) reverse string using for loop

# s = "hello"
# rev = ""
# for i in s[::-1]:
#     rev = rev + i
# print(rev)

#Question 37) check string is palindrome or not

# str1 = input("enter a string :")
# rev = (str1[::-1])
# if rev == str1:
#     print("string is palindrome ")
# else:
#     print("string is not palindrome")

# solve by function

# def palindrome(s):
#     rev = s[::-1]
#     if s == rev:
#         print(f"{s} is a palindrome ")
#     else:
#         print(f"{s} is not palindrome")

# palindrome("madam")



# Question 38) count number of vowel and consonants from a string
# s = "Golmaal"
# vowels = 0
# consonants = 0
# for i in s :
#     if i in "aeiouAEIU":
#         vowels += 1
#     else:
#         consonants += 1
# print(f"total vowels are : {vowels}")
# print(f"total consonants are : {consonants}")



#                         DATE --> 17 APRIL,2026

# Question 1) count the number of digits in a number

# n = 1234
# count = 0
# while n > 0:
#     digit = n % 10 #.  isko hata v sakte hai
#     count = count + 1
#     n = n//10
# print(f"count of digits is : {count}")

# OR.(solve by function)
# def count(n):
#     count = 0
#     while n > 0:
#         digit = n % 10 #.  isko hata v sakte hai
#         count = count + 1
#         n = n//10
#     print(f"count of digits : {count}")
# count(256)

# OR

# NOTE -- >>  yedi aap function me kahi v "return" lagaya to usse "print" karana parega
# def count(n):
#     count = 0
#     while n > 0:
#         digit = n % 10 #.  isko hata v sakte hai
#         count = count + 1
#         n = n//10
#     return f"count of digits : {count}"
# print(count(256))


""" NOTE -- >  if we use return inside a function it will act like a mini variable and until
unless we didn't print the vriable the output """

# Question 2) find the sum of digits of number 
# n = 123
# sum = 0
# while n > 0:
#     ld = n%10
#     sum = sum + ld
#     n = n //10
#     print(f"sum of digit is : {sum}")

# solve by function

# def sum(n: int):
#     sum = 0
#     while n > 0:
#         ld = n%10
#         sum = sum + ld
#         n = n // 10
#         return f"{sum}"
# print(sum(124))

#Question 3) check wether a number is armstrong number or not
# n = 153
# copy = n
# sum = 0
# while n > 0:
#     ld = n % 10
#     power = ld ** 3
#     sum = sum + power
#     n = n // 10
# if copy == sum:
#     print("armstrong number")
# else:
#     print("not armstrong number")



#.                                         DATE ==> 15 MAY,2026 



# def add(a,b,c):
#     print(a+b+c)

# add(10,20,30)

""" problem is what if hume hi nahi pata ki kitne parameters hone wale hai
solution -> args """

""" args -> *varible_name
variable_name -> chacha,mama,lolo kesa bhi likh sakte hai 
args values ko accept krte hi in the form of tuple"""

# def add(*a):  # * args
#     print(type(a))
#     print(a)
# add(10,20,30,40,50)


# using loops

# def add(*a):  # * args
#     for i in a:
#         print(i)
# add(10,20,30,40,50)


# key argument

# def polio(name,age,pin,contact):
#     print(name,age,pin,contact)
# polio(name="Ramesh",age=22,pin= 122,contact=0000000 ,grandfather ="lala") # inhe hum key argument bolte hai


""" kwargs --> keywords arguments
     denote --> **varible_name  --> ramesh ,chacha, doremon ,bhaubali
    kwargs --> accepts krte ahi sari values ko in the form of dictionary
    parameter woh --> keys
    arguments woh --> values"""

# def polio(**variable):
#     print(type(variable))
#     print(variable)
# polio(neme="suresh" ,age=21 ,school="dps")


# def polio(**a):
#     for i in a:
#         print(f"parameters -> {i} and Arguments -- {a[i]} ")
#         # i -> dict keys , a[i] --> un keys ki value
# polio(name="Suresh",age=21,school="dps")


"""" lambda funtion --> jab ek funtion ek line mai aa jay 
lambda --> keyword
a,b: a+b --> agar a and b variable me kuch value aayegi toh hi a+b chalega warna nhi chalega """

add = lambda a,b: a+b
print(add(10,20,))