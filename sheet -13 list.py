# Question 1) Ask the useer to enter a list of numbers and print the largest element
# n = int(input("how many elements you want to enter :"))
# l = []
# for i in range(n):
#     z = int(input("enter your number :"))
#     # i += 1
#     l.append(z)
# if len(l) > 0:
#     largest = l[0]
#     for i in range(1,len(l)):
#         if l[i] > largest:
#             largest = l[i]
#     print(f"print your largest number in list : {largest}")
#     print(f"list is : {l}")

# Question 2) Ask the user to enter a list and print the smallest element
# n = int(input('how amny element you want to print : '))
# l = []
# for i in range(n):
#     z = int(input("enter your number :"))
#     l.append(z)
# if len(l) > 0:
#     smallest = l[0]
#     for i in range(1,len(l)):
#         if l[i] < smallest:
#             smallest = l[i]
#     print(f"smallest number is : {smallest}")
#     print(f"the list of numer is : {l}")

#Question 3) Ask the user to enter a list and print sum of all elements
# n = int(input("how many element you want to print : "))
# l = []
# sum = 0
# for i in range(n):
#     z = int(input("enter your number : "))
#     l.append(z)
#     sum = sum + z
# print(f"the sum of number is : {sum}")

# Question 4) Ask the user to enter a list and count even numbers
# n = int(input("how many element you want to print :"))
# l = []
# even_count = 0
# for i in range(n):
#     z = int(input("enter your number : "))
#     l.append(z)
# for z in l:
#     if z % 2 == 0:
#         even_count += 1
# print(f"total number of even in list : {even_count}")

#Question 5) Ask the user to enter a list and count odd numbers
# n = int(input("how many element you want to print :"))
# l = []
# odd_count = 0
# for i in range(n):
#     z = int(input("enter your number :"))
#     l.append(z)
# for z in l:
#     if z % 2 != 0:
#         odd_count += 1
# print(f"total numbr odd in list : {odd_count}")

#Question 6) Ask the user to enter a list and reverse it.

# a = [10,20,30,40,50,60]
# z = len(a)-1

# for i in range(len(a)//2):
#     a[i],a[z] = a[z],a[i]
#     z = z-1
# print(a)

#  [OR]

# n = int(input("how many element you want to print : "))
# l = []

# for i in range(n):
#     z = int(input("enter your numbers : "))
#     l.append(z)
#     z = len(l) -1
# for i in range(len(l)//2):
#     l[i],l[z] = l[z],l[i]
#     z = z-1
# print(l)

# [OR]

# a = [10,20,30,40,50]
# l = []
# for i in range(len(a)-1,-1,-1):
#     l.append(a[i])
# print(l)

# [OR]
# n = int(input("how many element you want to print : "))
# l = []
# for i in range(n):
#     z = int(input("enter your number :"))
#     l.append(z)
# for i in range(len(l)-1,-1,-1):
#     print(l[i],end = " ")       

# QUESTION 7) Ask the user to enter a list and remove duplicates

# l = [29,2,2,2,12,14,29,31,12,56 ,5,5,78]

# dupli_list = []
# for element in l:
#     if element not in dupli_list:
#      dupli_list.append(element)

# print(f"the list with removed duplicate = {dupli_list}")

# [OR]

# n = int(input("how many element you want to print : "))
# l = []
# for i in range(n):
#    z = int(input("enter your number : "))
#    l.append(z)
# print(f"my list is : {l}")
# non_duplicate_value = set(l) # list ko set me rakhne par duplicate value remove ho jayegi
# print(f"after remove of duplicate value : {non_duplicate_value}")

#Question 8) Ask the user to enter a list and sort it in ascending order.

# l = [3,2,6,5,7,4,8,9]
# l.sort() #.   using sort() method in this question
# print(l)

#[OR]
# solve by without using method {solve by (Bubble sort) }

# n = int(input("how amny element you want to print :"))
# l = []

# for i in range(n):
#     z = int(input("entr your number : "))
#     l.append(z)

# for j in range(len(l)-1):
#     for i in range(len(l)-1-j):

#         if l[i] > l[i+1]:
#             l[i],l[i+1] = l[i+1],l[i]
# print(l)

# QUESTION 9) Ask the user ssto enter a list and find second largest element.

# n = int(input("how many element you want to print : "))
# l = []
# for i in range(n):
#     z = int(input("enter your number : "))
#     l.append(z)

# largest = l[0]
# largest_index = 0
# s_largest = l[0]
# s_largest_index = 0
# for i in range(1,len(l)):
#     if l[i] > largest:
#         s_largest = largest 
#         largest = l[i]
#         s_largest_index = largest_index
#         largest_index = i
# print(f"the largest mumber is : {largest}")
# print(f"the second largest number is : {s_largest}")
# print(f"the largest index of list : {largest_index}")
# print(f"the second largest of the list is : {s_largest_index}")

# QUESTION 10) Ask the user to enter a list and print elements at even index.

# n = int(input("How many element you want to print : "))
# l = []
# for i in range(n):
#     z = int(input("enter your number : "))
    # l.append(z)
# for i in range(len(l)):
    # if i % 2 == 0:

    #     print(f"the element at even index : {l[i]}")
        


"""              SHEET COMPLETED     """