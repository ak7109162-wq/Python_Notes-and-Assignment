# Question 1) create a set of 5 numbers and print it

# num = {1,2,3,4,5}  # if a curly braces is empty it act as dictionary and if value are written in curly braces it act as sets
# print(num)

# OR

# num = [1,2,3,4,5]
# print(set(num))

#Question 2) create a set from the list below and print it. what happen to duplicates

# l = [1,2,2,3,4,4,5]
# print(set(l)) 

 # yedi list me duplicate value hai to usko set me likh dene par duplication allow nhi karti hai
# Note ==> Set doesn't allow duplicate value but list allow doplicate alue

# Question 3) Find the number of element in the sets

# s = {10,20,30,40,50}
# print(f"the total length of sets : {len(s)}")


# Question 4) Add the number 6 to set and print the updated set.

# s = {1,2,3,4,5}
# s.add(6)
# print(s) # The append() method is specifically designed for lists, 

# Question 5) remove an element 30 from set and print the updated set

# s = {10,20,30,40,50}
# s.remove(30)  # or s.discard
# print(s)

# OR
# l = [10,20,30,40,50] # in list also use .remove
# l.remove(30)
# print(l)

# Question 6) check if "banana" is present in the set
# fruits = {"apple", "banana","mango"}

# if "banana" in fruits:
#     print("present")
# else:
#     print("not present")

# Question 7) Print each element of set using a loop

# s = {"red" ,"green","blue"}
# for i in s:
#     print(i)

# Question 8) find union of two sets

# a = {1,2,3}
# b = {3,4,5}
# result = a.union(b)
# print(result)

# union in sets convert into single value

# Question 9) Find the intersection of two sets
#INTERSECTION ==> find only common elements

# a = {1,2,3,4}
# b = {3,4,5,6}
# result = a.intersection(b)  # it find only common value
# print(result)

# Question 10) find the difference -- element in a that are not in b

# A = {1,2,3,4,5}
# B = {3,4,5,}
# result = A.difference(B)
# print(result)