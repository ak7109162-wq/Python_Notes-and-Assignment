# Question 1) print numbers from  1 to 5 using a for loop.
for i in range (1,6,1):  # start , stop , step
    print(i)

# Question 2) print number from 1 to 10.
for i in range (1 ,11,1):
    print(i)

#Question 3) print even number from 1 to 10 using foor loop
for i in range (1, 11):
    if i % 2 == 0:
        print(i)

# or 
for i in range (2 ,11 ,2):
     print(i)

# Question 4) print odd number from 1 to 10 using loop.

for i in range (1 ,11 ):
    if i % 2 != 0:
        print(i)

# Question 5) print numbers from 10 to 1(reverse oorder).
for  i in range (10 , 0, -1):
    print(i)

#  Question 6) print multiplication table of 2.
for i in range (2 , 21,2):
    print(i)

# Question 7) print table using for loop
a = int(input("please tell me a number :"))
for i in range (a , a*10+1 ,a):
    print(i)