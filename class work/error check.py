# #Question) guess number (GAME)
# import random
# machine = random.randint(1,50)
# for i in range(8):
#     abhishek = int(input("enter your number :"))
#     if machine == abhishek:
#         print("you wom")
#         break
#     if machine > abhishek:
#         print("too small go higher")
#     if machine < abhishek:
#         print("too higher go small")
# else:
#         print(f"you lose : the real number is :{machine}")

# # Question )check wether a number is aplindrome or not

# n = input("enter a number :")
# if n == n[:: -1]:
#     print(f"number is palindrome")
# else:
#     print(f"number is not palindrome")

# or  check a number is palindrome or not

# num = 1221
# if str(num) == str(num)[:: -1]:
#      print(f"number {num} is palindrome")
# else:
#      print(f"number {num} is not palndrome")

# # Question) fibonacci series

# n = int(input("entera a numeber :"))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     a ,b = b,a+b

# Question ) print the largest digit in a number
# n = int(input("enter a number : "))
# largest = 0
# for i in str(n):
#     a = int(i)
#     if a > largest:
#         largest = a
# print(largest)

# Question ) addition of two number using function

# def addition(a,b):
#     print(a+b)

# addition(10,20)
# addition(13,10)

#Question) check number is palindrome using function

# def palindrome(n):
#     copy = n 
#     rev = 0
#     while n != 0:
#         ld = n % 10
#         rev = rev * 10 + ld
#         n = n//10

#     if copy == rev:
#         print("number is palindrome")
#     else:
#         print("number is not palindrome")

#     palindrome(121)
#     palindrome(134)
#     palindrome(198891)

# # Question ) multiply using function
# def multiply(a,b):
#     print(a*b)
# multiply(12,67)

#  Question ) 

# def info(name, age, id = None):
#     print("info recieved")
# info("abhishek",24,234)


# # Question ) check number is armstrong number or not using function
# def armstrong(n):
#     copy = n
#     sum = 0
#     length = len(str(n))
#     while n != 0:
#         ld = n % 10
#         sum = sum + ld ** length
#         n = n // 10
    
#     if copy == sum:
#         print("number is armstrong number")

#     else:
#         print("number is not armstrong number")

# armstrong(145)
# armstrong(153)

# Question ) Reverse the string
# s = "shery"
# print(f"reverse of string :{s[::-1]} ")
# print(f"the length of string : {len(s)}")
# print(f"string in upper format : {s.upper()} ") 
# print(f"string in lower format : {s.lower()}")

# Question ) Solve by using recursion function
# def countvowels():
#      str1 = "Hello"
#      vowels = "aeiouAEIOU"
#      count = 0
#      for i in str1:
#         if i in vowels:
#             print(i)
#             count += 1
#      return f"total count of vowel are : {count}"
# print(countvowels())


# Question ) check a number is armstrong number or not
# n = int(input("enter a number : "))
# s = len(str(n))
# copy = n 
# sum = 0
# while n != 0:
#     ld = n % 10
#     sum = sum + ld ** s
#     n = n // 10
# if copy == sum:
#     print("number is armstrong number")
# else:
#     print("number is not armstrong number ")

# same question solve by function 

# def check_armstrong():
#     n = int(input("enter a number : "))
#     s = len(str(n))
#     copy = n 
#     sum = 0
#     while n != 0:
#          ld = n % 10
#          sum = sum + ld ** s
#          n = n // 10
    
#     if copy == sum:
#         return f"number is armstrong number"
#     else:
#         return f"number is not armstrong number "
# print(check_armstrong())
        
# Question->) sum of digit sove by function
# def digit_sum(n: int):
#     #n = int("enter a number : ")
#     sum = 0
#     while n > 0:
#         ld = n % 10
#         sum = sum + ld
#         n = n // 10
#     return f"sum of digit are : {sum}"
# print(digit_sum(123))
# print(digit_sum(143))

# OR.   Question->) find the sum of digits of number 
# n = int(input("enter a number : "))
# sum = 0
# while n > 0:
#     ld = n % 10
#     sum = sum + ld
#     n = n // 10
# print(f"sum of digit : {sum}")

# Question)==> Count the number of digits in a number by function
# def count_digits(n):
#     count = 0
#     while n > 0:
#         digit = n % 10
#         count = count + 1
#         n = n // 10
#     return f"count of digit : {count}"
# print(count_digits(1234))
# print(count_digits(4356))


#.TOPIC =         LIST

# a = 12
# b = 13
# c = 14 
# d = 15
# e = 16
# l = [a,b,c,d,e]
# print(l)

# special power of list and function
#1) Hetrogenous nature - means it can store any kind of data types at once
# l = [12 ,"hello", 12.67,True, print()]
#2) ordered - every element in a list has designated position
#3) mutale nature - you can change anything inside the list at any point of time
#4) Duplicates - you can store duplicate element inside list

# Reading list 
# a = [10,20,30,40,50]
# print(a[0] ,a[-1])  # indexing


# updating list 
# a = [10,20,30,40,70]
# a[-1] = 50
# print(a)

# l = [2,3,4,6,6,7,8]
# l[3] = 5
# print(l)

# delete list
# l = [10,20,30,40,50,60]
# del l[:5]
# print(l)

# creating loops on list
# l = [10,20,30,40,50]
# for i in l:
    # print(i)


# bassed on index 
# for i in range(0,len(l)):
    # print(l[i])

# Topic ==> method
# 1) append method 

# l = [1,2,3,4,5]
# l.append(6)
# print (l)

# 2) insert method 
# l = [10,20,40,50,60]
# l.insert(2,30)
# print(l)

# 3) clear method 

# l = [10,20,30,40,50] # if we want to clear hole list use clear method
# l.clear ()
# print(l)

# 4) pop method 
# if we want to remove particular element in a list
# l = [10,20,30,40]
# l.pop(1) #.      remove 20 from list
# saved = l.pop(1) # saved 30 in variable (30 come in place of index 1)
# print(l,saved)

# Question )
# a = [10,20,30,40,10]
# a.pop(1) # remove 20
# saved = a.pop(1) # save 30
# a.remove(10)  # remove 10
# print(a)  # print 40,10


#.Topic ==> sort without method (Bubble sort)

# a = [56,12,89,23,56,90,13]

# for j in range(len(a)-1):
#     for i in range(0,len(a)-1 -j):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
# print(a)
        
#Question 2) Bubble sort
# a = [12,25,46,87,3,9,28,36]

# for j in range(len(a)-1):
    # for i in range(0,len(a)-1-j):
        # if a[i] > a[i+1]:
            # a[i],a[i+1] = a[i+1],a[i]
# print(a)

#Question 3)
# a = [90,43,67,45,22,98,72,56,32]
# for j in range(len(a)-1):
#     for i in range(0,len(a)-1):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
# print(a)


#Question )
# a = [12,56,23,89,1,45,7,8,4,23]

# largest = a[0]
# index = 0
# for i in range(1,len(a)):
#     if a[i] > largest:
#         largest = a[i]
#         index = i
# print(f"largest element is {largest} at index {index}")

# Question ) print largest number 
# a = [90,85,80,77,42,33,45,23,45]

# largest = a[0]
# index = 0
# for i in range(1,len(a)):
#     if a[i] > largest :
#         largest = a[i]
#         index = i
# print(f"larget element is {largest} at index {index}")

# Question ) print largest number 
# a = [90,85,80,77,422,33,45,23,45]

# largest = a[0]
# index = 0
# for i in range(1,len(a)):
#     if a[i] > largest:
#         largest = a[i]
#         index = i
# print(f"largest element is {largest} at index {index} ")


# Question ) Find second largest number
# l = [12,16,13,19,25,66,44,78]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i

# print(f"the second largest number is : {sec_largest} and the largest number is : {largest}")

# TOpic  => print largest , second largest and index

# l = [1,16,17,23,2,89,45]
# largest_index = 0
# largest = l[0]
# second_largest = l[0]
# second_largest_index = 0

# for i in range (1,len(l)):
#     if l[i] > largest:
#         s_largest = largest
#         largest = l[i]
#         second_largest_index = largest_index
#         largest_index = i

#     elif l[i] > s_largest:
#         s_largest = l[i]
#         second_largest = l[i]
#         second_largest_index = i
# print(largest , largest_index)
# print(s_largest , second_largest_index)

# [OR]
# l = [99,58,102,54,78,62,71,98,66]
# largest_index = 0
# s_largest_index = 0
# largest = l[0]
# s_largest = l[0]

# for i in range(1,len(l)):
#     if l[i] > largest:
#         s_largest = largest
#         largest = l[i]
#         s_largest_index = largest_index
#         largest_index = i

#     elif l[i] > s_largest:
#         s_largest = l[i]
#         second_largest_index = i
# print(f"the largest number is : {largest} and the largest number of index is : {largest_index}")
# print(f"the second largest number : {s_largest} and the second largest index is : {s_largest_index}")


#.      QUESTION ON LIST
#Question 1) How many element you want to print

# a = int(input("how many elements you want to print in list :"))
# l = []
# for i in range (a):
#     z = int(input("tell your numbers : "))
#     l.append(z)
# print(l)

# a = int(input("how many element you want to print :"))
# l = []
# for i in range (a):
#     z = int(input("tell your numbers :"))
#     l.append(z)
# print(l)


#Question ) Reverse the list
# a = [10,20,30,40,50]
# l = []
# for i in range(len(a)-1,-1,-1):
#     l.append(a[i])
# print(l)

#Question) Reverse list without using extra space (by two pointer)
# a = [10,20,30,40,50,60]

# z = len(a)-1
# for i in range(len(a)//2):
#     a[i],a[z] = a[z],a[i]
#     z = z - 1
# print(a)

# Question) print positive and negative element of list
# a = [1,2,-4,-2,1,-5,-2,12,45,8]
# for i in a:
#     if i >= 0:
#         print(i)
# for i in a:
#     if i < 0:
#         print(i)

#   Bubble sort
# a = [56,12,89,23,56,90,13]
# for j in range(len(a)-1):
#     for i in range(0,len(a)-1-j):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
# print(a)

#Question )
# a = [12,56,23,89,1,45,7,8,4,23]
# largest = a[0]
# index = 0
# for i in range(1,len(a)):
#     if a[i] > largest:
#         largest = a[i]
#         index = i
# print(f"largest element is {largest} at index {index}")

# find largest and second largest
# l = [1,16,17,23,2,89,45]
# largest__index = 0
# largest = l[0]
# second_largest = l[0]
# second_largest_index = 0

# for i in range(1,len(l)):
#     if l[i] > largest:
#         s_largest = largest
#         largets = l[i]
#         second_largest_index = i
# print(largest,second_largest_index)
# print(s_largest ,second_largest_index)

# print smallest and second smallest 
# l = [92,16,17,23,2,89,45]
# smallest_index = 0
# smallest = l[0]
# s_smallest = l[0]
# s_smallest_index = 0

# for i in range(1,len(l)):
#     if l[i] < smallest:
#         s_smallest = smallest
#         smallest = l[i]
#         s_smallest_index = smallest_index
#         smallest_index = i

#     elif l[i] < s_smallest:
#         s_smallest = l[i]
#         s_smallest_index = i
# print(smallest , smallest_index)
# print(s_smallest ,s_smallest_index)
    
# Question ) check if list is sorted or not

# l = [2,1,3,4,5,6,7]
# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("list is not sorted")
#         break
# else:
#     print("list is sorted")

# Question ) check if list is sorted or not
# l = [4,5,6,7,8,9,3,5,7]
# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("list is not sorted")
#         break
# else:
#         print("list is sorted")


# Question ) given list is palindrome or not
# l = [2,3,4,19,28,4,3,2]
# for i in range(len(l)//2):
#     if l[i] != l[len(l)-1-i]:
#         print("list is not palindrome ")
#         break
# else:
#     print("list is palindrome") 

# Question ) Take n as input from user

# n = int(input("enter the size :"))
# l = []
# sum = 0
# for i in range(n):
#     z = int(input(f"enter the element "))
#     sum = sum + z
#     l.append(z)
# print(f"the list of element is: {l}")
# print(f"the sum of list is : {sum}")

#[OR]

# lst = list(map(int,input("enter elements : ").split()))
# print(lst)

# map(data_type,input)
# split (seperates all the value and digits)
# list(converts the value in the form of list data structure )





""".                 DICTIONARY                        """

"""A Dictionary is a collection of key- value pairs accesed by a unique key"""

# QUestion ) 
# d = {}
# print(type(d)) #  type is dict
#Question)
# d = {1,2,3,4}
# print(type(d)) # type is set

# Question)
# d = {10:100,20:200,30:300,40:400}
# print(d[10])

# del d[40]
# print(d)

# Question ) 
# d = {10:100,20:200,30:300,40:400}
# d.update({50:500}) # this is the property of mutabality
# print(d)

#Question )
# d1 = {1:10,2:20,3:30}
# d1[4] = 100
# d1[5] = 400  # add multiple keys and value in dictionary
# print(d1)
# print(d1.items())
# print(d1.keys())
# print(d1.pop(3))

# Question 1) Write a python script to merge two python dictionaries

# d1 = {1:10,2:20,3:30}
# d2 = {4:40,5:50,6:60}

# for i in d2:
#     d1[i] = d2[i]
# print(d1)

# Question 2) write a python program to combine two dictionary by values for comman keys

# d1 = {1:10,2:20,3:30}
# d2 = {3:40,5:50,6:60}

# for i in d2:
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]
# print(d1)

# Question 3) count the frequency of each element

# l = [1,1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,6,6,6,6]

# d = {}
# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)

# Question 4) write a python program  to sum all the values in a dictionary
# d1 = {10:500,20:200,30:600,70:800}
# sum = 0
# for i in d1:
#     sum = sum + d1[i]
# print(sum)

# Question 5) 

# d1 = {1:10,2:20,3:30}
# d2 = {3:40,5:50,6:60}

# for i in d2:
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]
# print(d1)


#                Leetcode problem ww

# n = int(input("enter your number : "))
# result = []
# count = 0
# for i in range(1,n//2+1):
#     if n % i == 0:
#         count += 1
#         result.append(i)
#     if n // i != i:
#         result.append(n//i)
#         count += 1
        
# print(count)
# print(result)

# Solve by function 
# from math import sqrt

# def factors():
#     n = int(input("enter your number : "))
#     result = []
#     for i in range(1, int(sqrt(n)) + 1):
#         if n % i == 0:
#             result.append(i)
#             if n // i != i:
#                 result.append(n // i)
#     return sorted(result)
# print(factors())

#.  Question) find the number frequency

 #if a number is prsent betwee 1 to 10 then it is applicable

# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# hash_list = [0] * 11
# for i in n:
#     hash_list[i] += 1

# for i in m:
#     if i < 1 or i > 10:
#             print(f"the number which present in list n {i} : {0} times")
#     else:
#         print(f"the number which present in list n {i}: {hash_list[i]} times ")


# Question) count the frequency of each element in a list

# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# d = {}
# for i in n :
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# for j in m:
#     if j in d:
#         print( j, "->",d[i])
#     else:
#         print(j, "->", 0)

# function special topic 

# question ) add number by function

# def add(a,b,c):
#     print(a+b+c)

# add(10,20,30)

"""problem is what yedi hume pata nhi ahi hai ki parameters  kitne hai .. to is solution
--> args"""

"""args --> *variable_name  
variable_name kuch v le sakte hai succh as chacha , mama, lolo kuch v likh sake hai

args --> value ko accept karta hai in the form of tuples """

# def add(*a):
#     for i in a:
#         print(a)
# add(10,20,30,40)


# key arguments 

# def polio(name, age, pin,contact):
#     print(name,age,pin,contact)
# polio(name ="ramesh",age=22,pin= 4620,contact= 00000)


"""kwargs ---keywords arguments 
denote --> **variable_name 
kwargs --> accept krte hai sari value ko in the form of dictionary
paremeter --> keys 
argument --> values"""

# def polio(**a):
#     print(a)
# polio(name = "abhishek",age=12,school="dps", )


# def polio(**a):
#     for i in a:
#         print(f"parameter --> {i} and arguments --> {a[i]}")
#         # i --> dict keys ,a[i] --> un keys ki values

# polio(Name = "suresh", Age = 22 , School = "dps")


""" lambda function --> jab ek function ek line me aa jay
lambda  --> keyword use karte hai """

# add = lambda a,b : a+b
# print(add(10,20))


#                                   TOPIC ==> object oriented program

# class sharmavishnu:
#     def sample():
#         print("this is sample function")
# sharmavishnu.sample()


# class sharmavishnu:
#     def sample():
#         print("this is sample function")
    
# sharmavishnu.sample()
# print(sharmavishnu)


# Question )

# class Animal:
#     name = "Abhi"

    # def greet(self):  # jab bhi class ke andar ke function ko object ke help se call karoge toh
# toh ek parameter start karna hoga "self is a parameter"

        # print("this is animal class")

# tau = Animal() # class ko varible me store kar rahe hai isi ko object kahte hai aur ishi liye self ka use karte hai
# tau.greet()
# print(tau.name)

# Question ) Create a class which will perform 2 task
#1) Greet the user -"Hello from sample class"
#2) adding upto two number

# class sample:
#     def greet(self):
#         print("Hello from sample class ")

#     def add(self):
#         print("add two number")
#         a = 10
#         b = 20
#         print(a+b)

#     def multip(self):
#         a = 20
#         b =10
#         print(a*b)

#     def sub(self):
#         a = 90
#         b = 20
#         print(a-b)

#     def divide(self):
#         a = 20
#         b = 10
#         print(a/b)

# obj = sample()
# obj.greet()
# obj.add()
# obj.multip()
# obj.sub()
# obj.divide()



#.    Calculator ( using  concept of object oriented programig)

class calculator:
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a * b
    
    def divide(self,a,b):
        if b == 0:
            return
        return a /b
    
calc = calculator()
while True:
 
# a = int(input("enter first number"))
# b = int(input("enter second number "))

    print("for adding click --> 1 ")
    print("for subtract press --> 2 : ")
    print("for multiply press --> 3")
    print("for divide press --> 4")
    print("for exit press --> 5")

    choice = int(input("enter your choice (1 to 5) : "))

    if choice == 5:
        print("Calculator Closed")
        break



    a = int(input("enter first number : "))
    b = int(input("enter second number :  "))

    if choice == 1:
        print(f"Result :  {calc.add(a,b)} ")

    elif choice == 2:
        print(f"Result : {calc.sub(a,b)}")

    elif choice == 3:
        print(f"Result : {calc.multiply(a,b)}")
    
    elif choice == 4:
        print(f"Result : {calc.divide(a,b)}")
    else:
        print("invalid choice")