# Question 1) Ask the user to enter a number and check if it is positive.
num = float(input("enter a number : "))

if num > 0:
    print("the number is positive ")

elif num == 0:
    print("the number is zero ")

else:
    print("the number is negative")
    
# # Question 2) Ask the user to enter a number and if it is negative.
num = float(input("enter a number :"))

if num < 0:
    print(f"{num} - is a negative number")

elif num == 0:
    print("the number is equal to zero")

else:
    print(f"{num} is a positive number ")

# Question 3) Ask the user to enter a number and check if it is even or odd.
number = int(input("tell me your number :"))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Question 4) Ask the user to enter a number and check if it is greater than 10.
number = float(input("enter a number for checking number is greater than 10 or not :  "))
if number > 10 :
    print(f"{number} is greater than 10")
elif number == 10:
    print("the number is exactly 10. ")
else:
    print(f"{number} : is less than 10 ")

# Question 5) Ask the user to enter a number and check if it is equal to 0.
number = float(input("enter a number :"))
if number == 0:
    print("the number equal to zero")

elif number > 0:
    print(f"{number} is greater than zero")

else:
    print(f"{number} is less than zero")

# Question 7) Ask the user to enter two numbers and print the smaller number
nums1 = float(input("enter first number :"))
nums2 = float(input("enter second number :"))

if nums1 > nums2:
    print("nums2 is smaller ")
elif nums1 == nums2:
    print("Both numbers are equal")
else:
    print("nums1 is smaller")

# Question 6) Ask the user to enter two number and print the greater number.
nums1 = float(input("enter first number "))
nums2 = float(input("enter second number :"))
if nums1 > nums2:
    print("nums1 is greater")
elif nums1 == nums2:
    print("both number are equal")
else:
    print("nums2 is greter ")

# Question 8) Ask the user to enter their age nd check if they are eligible to vote.
name = input(" tell me your name :")
age = int(input("tell me your age : "))

if age >= 18:
    print(f"Hello {name} you are a valid voter you can vote ")

else:
    print(f"Hello {name} you can't be vote because your age is below 18 , \n you can vote after {18 - age} years ")

# Question 9) Ask the user to enter a number and check if it is divisible by 5.
number = int(input("enter a number : "))
if number % 5 == 0:
    print(f"{number} is divisible by 5.")

else:
    print(f"{number} is not divisible by 5")

#Question 10) Ask the user to enter a number and check if it is divisible by 2 and 3.
number = int(input("enter a number :"))
if (number % 2 == 0) and (number % 3 == 0):
    print(f"{number} is divisible by 2 and 3")

else:
    print(f"{num} is not divisible by 2 and 3.")

# Question 11) Ask the user to enter marks and check pass or fail(pass if >= 40).
marks = float(input("enter marks : "))
if marks >= 40:
    print(f"your marks{marks} is greater than 40 : pass")
else:
    print(f"your marks{marks} is below 40 : fail")

# Question 12) Ask the user to enter a number and check if it is between 1 and 100 .
number = float(input("enter a number : "))
if (number >= 1) and (number <= 100):
    print(f"{number} number lie between 1 to 100 ")
else:
    print(f"{number} number not lies between 1 to 100")

# Question 13) Ask the userto enter temoerature and check if it is hot (>30) or cold
temperature = float(input("enter the temperature in °c :"))
if temperature > 30:
    print(f"{temperature} is greater than 30°c so it is hot")
else:
    print(f"{temperature} is less thsn 30°c so it is cold ")

#Question 14) Ask the user to enter a number and check if it is multiple of 10
number = int(input("Enter a number for checking that is multiple of 10 :"))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10 ")

# Question 15) Ask the user to enter a number and check if it is less than 0, equal to 0, or greater than 0
nums = float(input("enter a number to check number is less than 0 ,equal to 0, or greater than 0 : "))
if nums > 0:
    print(f"{nums} is greater than 0 ")

elif nums == 0:
    print("it is equal to zero")
else:
    print(f"{nums} is less than zero")


#   (IF - ELIF - ELSE)  SHEET COMPLETE 

print(" 'IL' - 'ELIF' -'ELSE'    STATEMENT SHEET COMPLETE ")


