# # Question 1) Accept an integer and print hello world n times
n = int(input(" enter a number to print number of string :"))
for i in range(1,n+1):
    print("hello world")

# Question 2) print natural number up to n.
n = int(input("enter a number upto print n : "))
for i in range(1 , n+1):
    print(i)

# # Question 3) Reverse for loop. print n to 1
num = int(input("tell me your number for reverse : "))
for i in range(num, 0 ,-1):
    print(i)

# Question 4) Take a number as input and print its table.

n = int(input("enter a number to print a table : "))
for i in range(1 ,11):
    print(f"{n} x {i} = {n * i}")

# Question 5) sum up to n terms
n = int(input("enter a number : "))
a = 0
for i in range(1 , n+1):
    a = a + i
print(f"the sum of n terms is : {a}")

# # Question 6) Factorial of a number
n = int(input("enter a number to find out factorial : "))
a = 1 
for i in range(1 , n+1):
    a = a * i 
print(f"factorial of n terms is :{a}")

# Question 7) print the sum of all even & odd numbers in range seperatly
