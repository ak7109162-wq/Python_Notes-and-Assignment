#.                            DATE => 28 APRIL,2026
# Topic => Dictionary 

"""# A Dictionary is a collection of key-value pairs accesed by a unique key
# And A list is an ordered sequence of element accesed by their numeric index
# In python hashmap is also known as dictionary 

#        dictionary power  
# 1) mutable - dictionaries are mutable. meaning you can change,add or remove key value pairs
# 2) duplicate - keys must be unique . but you can have duplicate in value
# 3) order - dictionary follow insertion order
# 4) heterogeneous - A dictionary can store different types of keys and values like integers ,strings ,lists or even another dicttionary"""

#QUESTION)
# d = {}     # jab empty space ho to set hota hai
# print(type(d))  # output dictionary

#QUEESTION)
# d = {1,2,3,4}
# print(type(d)) # output set jab hum dict me value dal dete hai to set ban jata hai

#QUESTION)
# d = {10:100,20:200,30:300,40:400}
# print(d[10]) # dictionary ke index nhi hota key ke through hi value access kar sakte hai

#QUESTION )
# d = {10:100,20:200,30:300,40:400}
# d[10] = 1000 # update value of 10
# del d[30]  # del delete the key and value both
# print(d)

# Question)

# d = {10:100,20:200,30:300,40:400}
# d.update({50:500})
# print(d)

#QUESTION)
# d1 = {1:10,2:20,3:30}
# d1[4] = 100 
# # print(d1)
# # print(d1.items())
# # print(d1.kesys())
# print(d1.pop(3))
# print(d1.setdefault(4,40))

 # Question 1)  Write a python script to merge two pytho dictionaries
# d1 = {1:10,2:20,3:30}
# d2 = {4:40,5:50,6:60}

# for i in d2:
#     d1[i] = d2[i]
# print(d1)

# Question 2 ) write a python program to combine two dictionary by values for common keys
# d1 = {1:10,2:20,3:30}
# d2 = {3:40,5:50,6:60}

# for i in d2:
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]
# print(d1)

# # Question 3) count the frequency of each element 
# l = [1,1,1,2,2,2,2,3,4,5,5,5,5,6,6,6]
# d = {}
# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)
 
# Question 4) write a python program to sum all the values in a dictionary

# d1 = {10:100,20:200,40:300}
# sum = 0
# for i in d1:
#     sum = sum + d1[i]

# print(sum) 

 
#.                        DATE => 29 APRIL,2026


# a = {1:10,2:20,3:30}
# b = {3:40,5:50,6:60}

# for i in b:
#     if i in a.keys():
#         a[i] =a[i] + b[i]
#     else:
#         a[i] = b[i]
# print(a)



#.                                     DATE => 30 APRIL,2026

# leetcode problem - 2206

# l = [3,2,3,2,2,2]

# d = {}
# for i in l:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# for i in d.values():
#     if i % 2 != 0:
#         print("not pair")
#     else:
#         print("pair")
