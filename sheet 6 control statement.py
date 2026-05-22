#Question 1) Ask the user to enter a number and check if is even or odd
num = int(input("enter a for number for checking odd or even : "))
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is an odd number ")

# Question 2) Ask the user to enter a number and check if it is positive , negative or zero
number = float(input("enter a number : "))
if number > 0:
    print(f"{number} is positive ")
elif number < 0:
    print(f"{number} is negative ")
else:
    print("number is equal to zero")

# Question 3) Ask the user to enter two numbers and print the greater number
nums1 = float(input("enter 1st number :"))
nums2 = float(input("enter 2nd number :"))
if nums1 > nums2:
    print(f"the great number is : {nums1}")
elif nums2 > nums1:
    print(f"the greater number is : {nums2}")
else:
    print("both are equal .")

#Question 4) Ask the user to enter a number and print numbers from 1 to that number using loop.
num = int(input("enter a number and print numbers from that number : "))

i = 1
while i <= num:
    print(i)
    i += 1

# Question 5) Ask the user to enter a number and print its multiplication table
num = int(input("enter a number for which you want to print multiplication : "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

# Question 6) Ask the user to enter a number and print sum from 1 to n.
# Question 7) Ask the user to enter a number and check if it is divisible by 2 and 3.
nums = int(input("enter a number : "))
if (nums % 2 == 0) and (nums % 3 == 0):
    print(f"{nums} is divisible by 2 and 3")
else:
    print(f"{nums} is not divisible by 2 and 3")

# Question 8) Ask the user to enter a number and count digits using loop.
number = int(input("enter a number :"))
i = 1
while i <= number:
    print(i)
    i += 1

# Question 9) Ask the user to enter a number and print reverse of number.
number = int(input("enter a number : "))
i = 0
while number > 0:
    ld = num % 10
    reverse = (i * 10 + ld)
    number //= 10
    print("reversed number :" ,reverse)

#Question 10) Ask the user to keep taking input until user enters 0 and print total sum