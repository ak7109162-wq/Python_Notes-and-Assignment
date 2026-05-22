# # Question 1) Ask the user to enter and print sum of first n natural numbers
n = int(input("Enter a number to print sum of 'n' natural number : "))
a = 0 
for i in range(1 , n+1):
    a = a+i
print(a)

 # # Question 2) Ask the user to enter a number and print factorial of that number.
num = int(input("enter a number : "))
a = 1
for i in range(1 ,num +1):
    a = a * i
print(f"the factorial of {num} is: {a}")

# # Question 3) Ask the user to enter a number and print all even numbers up tp that number.

n = int(input("enter a number : "))
for i in range(1 , n+1):
    if i % 2 == 0:

     print(f"total number of even number is : {i}")

# Question 4) Ask the user to enter a number and print all odd number up to that number.

n = int(input("enter a number : "))
for i in range(1 , n+1):
    if i % 2 != 0:
     print(f"total number of odd number is : {i}")

# # Question 5) ask the user to enter a number and print number divisible by 5 up to that number

n = int(input("enter a number : "))
for i in range(1 ,n+1):
   if i % 5 == 0:
      print(i)

# # Question 6) Ask the user to enter a number and print the sum of evan numbers up to that number

n = int(input("enter a number : "))
a = 0
for i in range(1 , n + 1):
   if i % 2 == 0:
      a = a + i    
print(f"the sum of even number upto that number is : {a}")

# # Question 7) Ask the user to enter a number and print the product of numbers from 1 to n.

n = int(input("tell me your number :"))
a =1 
for i in range(1 , n+1):
   a = a * i
print(a)

# # # Question 8) Ask the user to enter a number and print square of number from 1 to n.
n = int(input(" tell me your number : "))
a = 2
for i in range(1 , n+1):
   square = i ** a
   print(f"square of number is : {square}")

# # Question 9) Ask the user to enter a number and print summ of odd number up to n.
n = int(input("tell me your number :"))
a = 0
for i in range(1 , n+1):
   if i % 2 != 0:
      a = a + i
print(a)

# Question 10) Ask the user to enter to enter a number and print reverse of that number using loop.
n = int(input("enter a number : "))
for i in range (n, 0,-1):
    print(f"the reverse output : {i}")

#   SHEET -- - 10 (COMPLETED)


print("SHEET - 10 COMPLETED")

# Question 11) check wether a number is prime number or not 

n = int(input("enter a number to findout number is prime or not : "))
count = 0
for i in range(1 , n+1):
   if n % i == 0:
      count = count + i

   if count == 2:
      print(" a number is prime number ")
   else:
      print(" a number is compsite number")

                     #   or

n = int(input("tell me your number : "))

for i in range(2 , (n//2)+1):
   if n % i == 0:
      print("your number is not prime")
      break
else:
      print("your number is prime")

# Question 12) check wether a number is special number or not

n = int(input("Tell me your number for checking a number is special number or not :"))
sum = 0
for i in range(1 , n ):
   if n % i == 0:
      sum = sum + i
if sum == n:
   print("a number is special number ")
else:
   print("a number is not a special number")
