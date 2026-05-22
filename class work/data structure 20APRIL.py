#.                              DATE ==> 20 APRIL, 2026
# TOPIC ==> DATA STRUCTURE
"""datastructure are used to store ,organize and manipulate data efficiently.
python provide several built in data structure 
In python four type of built in data structures(list,tuple,set, dictionary)"""
 
#.   LIST ==> 

# a = 12
# b = 13
# c = 14
# d = 15
# e = 16
# for creating list you have to use square bracket ([])

# l = [12,13,14,15,16]

# special power(function)
#1) hetrogeneous nature - means it can store any kind of data types at once
# l = [12, "hello ",12.67,True, print()]

#2) ordered - every element in list has a designated position
#3) mutable nature  - you can change anything inside the list at any point of time

# 4) duplicates -- you can store duplicate element inside list

"""if we want to know all method then we write print(dir(list))"""

# reading list
# a = [10,20,30,40,50]
# you  will indexing 
# print(a)
# print(a[4], a[-1])

# updating list 
# a = [10,20,30,40,40,70 ]

# a[-1] = 50
# print(a)


# delete list
# a = [10,20,30, 40, 50]
# you can delete a single element and entire list
# del a[-1]
# print(a)


#creating loops on list
a = [10,20,30,40,50]
 # based on values
# for i in a:
    # print(i)
# here you will access all the values 10,20,30,..

# based on index

# for i in range(0,len(a)):  # or 5
#     print(a[i])

# this loop can access your index as well as your values and it givess more control over list


# TOPIC ==> methods 
# a = [1,2,3,4]
# a .append(5)
# print(a)

# Question)
# l = []
# for i in range(10,51,10):
#     l.append(i)

# print(l)


# insert method

# a = [10,20,40,50]  # jab beech me kuch add karna ho
# a.insert(2,30)
# print(a)

# clear method
# a = [10,20,30] # pura list clear ho jayega
# a.clear ()
# print(a)

# particular element remove
# a = [10,20,30,40]
# a.pop(0)
# saved = a.pop(0)
# print(a)

# a = [10,20,30,10]
# saved = a.pop(1) # this will remove via index
# a.remove(10) # this will remove via value
# print (a)



#.                           DATE ==> 21 APRIL ,2026

# indexing
# a = [10,20,30,40,50]
# print(a.index(50))

# reverse
# a = [10,30,50,30,20]
# a.reverse()
# print(a)

# sort ==> it convert into ascending order
# a = [10,20,40,30,50]
# a.sort()
# print(a)


#                QUESTION ON LIST

# Question 1) how many element you want

# a = int(input ("how many elments you want : "))
# l = []

# for i in range (a):
#     z = int(input("tell your numbers : "))
#     l.append(z)
#     l.sort()

# print(l)
# OR 
# a = eval(input("tell your str"))
# print(a)


#.  REVERSE the list

# a = [10,20,30,40,50]
# l = []
# for i in range(len(a)-1,-1,-1):
#     l.append(a[i])
# print(l)

# reverse list without usin extra space (by two pointer)
# a = [10,20,30,40,50]

# z = len(a) - 1

# for i in range(len(a)//2):
#     a[i],a[z] = a[z] ,a[i]
#     z = z - 1
# print(a)


#question ) print postive and negative element of list

# a = [1,2,-4,-2,1,-5,-2,12,45,8]

# for i in a:
#     if i >= 0:
#         print(i)
# for i in a: 
#     if i < 0:
#         print(i)


#.                         22 APRIL ,2026

# sort without method 
# (Bubble sort)

# a = [56,12,89,23,56,90,13]

# for j in range(len(a)-1):
#     for i in range(0, len(a)-1 - j):
#         if a[i] > a[i+1]:
#          a[i],a[i+1] = a[i+1],a[i]
# print(a)

# Quesstion )
# a = [12,56,23,89,1,45,7,8,4,23]

# largest = a[0]
# index = 0
# for i in range (1,len(a)):
#    if a[i] > largest:
#       largest = a[i]
#       index = i

# print(f"largest element is {largest} at index {index}")
   


#.                                    DATE ==> 23 April 2026

# l = [1,16,17,23,2,45,89]

# largest = l[0]
# s_largest = l[0]
# for i in l:
#     if i > largest:
#         s_largest = largest
#         largest = i
# print(largest)
# print(s_largest)

# print second largest and index
# l = [1,16,17,23,2,89,45]
# largest_index = 0
# largest = 1[0]
# second_largest = 1[0]
# second_largest_index = 0

# for i in range(1,len(1)):
#     if l[i] > largest:
#         s_largest = largest
#         largest = 1[i]
#         second_largest_index = largest_index
#         largest_index = i

#     elif l[i] > s_largest:
#         s_largest = l[i]
#         second_largest = l[i]
#         second_largest_index = i
# print(largest, largest_index)
# print(s_largest ,second_largest_index)

# print smallest and second smalllest and index also

# note ==> for finding smallest and s_smallest -> you will pick greater value 
# for finding largest and s_smallest _> you will pick smaller vaue 
# l = [1,16,17,23,2,89,45]
# smallest_index = 0
# smallest = l[0]
# second_smallest = l[0]
# second_smallest_index = 0

# for i in range(1,len(l)):
#     if l[i] < smallest:
#         s_smallest = smallest
#         smallest = 1[i]
#         second_smallest_index = largest_index
#         largest_index = i

#     elif l[i] < s_smallest:
#         s_smallest = l[i]
#         second_smallest = l[i]
#         second_smallest_index = i
# print(smallest, smallest_index)
# print(s_smallest ,second_smallest_index)


#.                          DATE => 24 APRIL 2026

# QUestion => check if list is sorted or not

# l = [2,1,3,4,5,6,7]
# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("list is not sorted")
#         break

# else:
#     print("list is sorted")


# Question ) palindrome => left to right or right to left
# l = [2,3,15,15,3,2]
# for i in range(len(l)//2):
#     if l[i] != l[len(l)-1-i]:
#         print("list is not palindrome")
#         break
# else:
#     print("list is palindrome")

""" Question. ---
# Task => take n as input from user 
# 2) create an list of size n
#3) take input for each element"""

# n = int(input("enter the size"))
# l = []
# sum = 0
# for i in range(n):
#     inputs = int(input(f"enter the element at index {i}"))
#     sum += inputs
#     l.append






#[OR] 
# lst = list(map(int,input("enter elements : ").split()))
# print(lst)

#map(data_type,input)
#split(sepereates all the value and digits)
# list(converts the value in the form of list data structure)

""" sabse pehle input accept -> har input split hoga-> inputs will be type
casted in the form of int -> we stored  all the int values inside a list. """


#.                                DATE => 27 APRIL 2026

# rotate a list by k elements 
# l = [1,2,3,4,5]  #o//p = k=2,[4,5,1,2,3]
# k = 2
# for i in range(k):
#     last = l[-1] # last value 5
#     for j in range(len(l)-1,0,-1): # j -> 4,3,2,1
#         l[j] = l[j-1]
#     l[0] = last
# print(l)

# Question ) assign all the 0s at the end of the list
# l = [0,1,0,3,12]
# j = 0
# for i in range(len(l)):
#     if l[i] != 0:
#         l[i],l[j] = l[j],l[i]
#         j = j+1
# print(l)



#                                                DATE => 28 APRIL,2026

