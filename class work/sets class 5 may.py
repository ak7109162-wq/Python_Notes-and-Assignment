#.  TOPIC ==>    SETS.
""" 1.unordered (no indexing)
2. semi-mutable(can add , but cannot change)
3. unique element (no duplicate)
4. heterogeneous (can contain different data type ) """

# a = [] # list
# b = {}  # enpty behave like dictionary
#print(type(b))

# c = set() # type conversion
# s = set()  # empty set
#s = {1,2,3,4,5} # after add elment it become set
# print(type(s))


# topic ==> method in sets

#1). add(). -- for adding single element / value
# s = {1,2,3,4,5,}
# s.add(6)
# print(s)

#2.) update() --- for adding multiple element / value in set

# s = {1,2,3,4,5}
# s.update([7,8,9])  # if you use update method then write element in list
# print(s)  

# 3) remove() --- if value is not present we will give an error

# s = {1,2,3,4,5}
# s.remove(1)
# print(s)

# 4.) discard() --  if element is not present in list then not gave error

# s = {1,2,3,4,5}
# s.discard(7)
# print(s)

#5.) pop() -- remove smallest elements

# s = {8,2,3,4,5}  
# print(s.pop()) # remove smallest element

# 6.) clear() --  removes all the elements and give us an empty set

# s = {1,2,3,4,5}
# s.clear()
# print(s)

# ************. ADVANCE METHODS OF SETS *****************

# 1.)   intersection

# s1 = {1,2,3,4}
# s2 = {2,3,4,6}
# print(f"intersection : {s1.intersection(s2)}") # - give comman value 

# 2.) union 

# s1 = {1,2,3,4}
# s2 = {2,3,4,6}
# print(f"union : {s1.union(s2)}") # convert common value into single value

# 3) difference 

# s1 = {1,2,3,4}
# s2 = {2,3,4,6}

# print(f"diiference s1 : {s1.difference(s2)}")
# print(f"difference s2 : {s2.difference(s1)}")  # find the value which not present in s1 and s2

# 4) symmetric diffrence

# s1 = {1,2,3,4}
# s2 = {2,3,4,6}
# print(f"symmetric_difference : {s1.symmetric_difference(s2)}")
#-- remove common value and give the unique value from the set

# 5) Frozen set 

# fs = {10,20,30,40,50}
# fs = frozenset(fs)
# fs.add(60)
# fs.remove(10) #--- cannot add or remove elements it can be static



#.                           DATE ==> 5 MAY,2026

