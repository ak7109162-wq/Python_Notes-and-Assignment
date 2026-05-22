# Topic ==> Tuples
""" 1. tuples are ordered (indexing)
 2. can have duplicacy
 3. are hetrogeneous
 4. are immutable 
 """

# t = () # empty tuple
# direct loopn{}
# t = (1,2,3,4,5)
# for i in t:
#     print(i)

# # index loop
# for i in range(len(t)):
#     print(i ,t[i])


# t = (1,2,3,4,5)
# for index, value in enumerate(t):
#     print(index,value)  # give both index and element


# t = (1,2,3,4,5)
# print(t[2])
# print(t[1:4]). # slicing in tuples

""" method in tuples
    1. count()
    2. index()"""

# t = (1,2,2,2,2,3,4,5,3,4)
# print(t.count(2))
# print(t.count(3))

# print(t.index(1))
# print(t.index(2)) # first occuerence of 2 


# membership operator

# t = (1,2,2,2,3,4,5,3,4)
# print(3 in t) # membership operator
# print(9 in t)


# TUple  packing and unpacking

# t = (1,2,3,4,5)
# a,b,c,d,e = t # unpacking
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a = 1,2   #this is packing


#      star Expression(*)
# t = (1,2,3,4,5)
# a,*b = t
# print(a)
# print(b) # remaining value print

# t = (1,2,3,4,5)
# a,*b,c = t   # c = 5 and b =2,3,4 and a= 1 --- Output
# print(a)
# print(b) # Middle value extraction
# print(c)


# merge two tuples
# t1 = (1,2,3)
# t2 = (4,5,6)
# print(t1+t2)



