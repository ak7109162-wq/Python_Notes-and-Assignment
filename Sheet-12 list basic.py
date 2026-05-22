# Question 1) create a list of 5 numbers and print the list
a = int(input("enter your 1st number :"))
b = int(input("enter your 2nd number :"))
c = int(input("enter your 3rd number :"))
d = int(input("enter your 4th number :"))
e = int(input("enter your 5th number :"))
l = [a,b,c ,d ,e,]
print(f"list of number is : {l}")

#[OR] SOlve by for loop
a = int(input("How many element you want to print :"))
l = []
for i in range(a):
    z = int(input("enter your number "))
    l.append(z)
print(z)

# [OR]
l = []
for i in range(10,60,10):
    l.append(i)
print(l)

# QUESTION 2) create a list of 3 fruit and print each item
a = int(input("How many fruit you want to print : "))
l = []
for i in range (a):
    z = input("enter your fruit name : ")
    l.append(z)
print(l)

# QUESTION 3) Create a list and print the first element

l = [10,20,30,40]
print(l[0])

# [OR] important
a = int(input("how many element you want to print : "))
l = []
for i in range(a):
    z = int(input("enter your number : "))
    l.append(z)
print(f"the first element of list is : {l[0]}")

# QUESTION 4) create a list and print last element

a = int(input("How many element you want to print : "))
l = []
for i in range(a):
    z = int(input("enter your number : "))
    l.append(z)
print(f"the last number of list : {l[-1]}")

# QUESTION 5) Create a list and print its length
# a = input("enter a number : ")
# list = a.split()
# print(list)
# print(len(list))

# [OR]

# n = int(input("how many element you want to print :"))
# l = []
# for i in range(n):
#     z = int(input("enter your number : "))
#     l.append(z)
# print(f"list is : {l} and the length of list is : {len(l)}")


# Question 6) create a list and add a new element at the end
# l = [99,55,87,66,77,95]
# l.append(91)  # yedi last me koi element add karna ho .append ka use karte hai
# print(l)

# Question 7) create a list and remove an element.

# a = int(input("how many element you want to print : "))
# l = []
# for i in range(a):
#     z = int(input("enter your number : "))
#     l.append(z)
# l.pop(2)  # by .popmethod we remove 2 from the list
# print(l)

#Questio 8) Create a list and check if a value exists in it.
# l = [10,20,30,40,50,60]
# check = int(input("enter your number : "))
# if check in l:
#     print("value exist")
# else:
#     print("value not exist")

# Question 9) create a list and print sum of all element 
# l = [5, 6, 7, 8, 9, 10]
# for i in l:  # actual number ko print karta hai
#     print(i)

# Question 10) create a list and print sum of all element
# n = int(input("how many element you want "))
# l = []
# sum = 0
# for i in range(n):
#     z = int(input("enter your number : "))
#     sum = sum + z
#     l.append(z)
# print(l)
# print (sum)

