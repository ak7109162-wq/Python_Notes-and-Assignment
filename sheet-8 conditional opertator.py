# Question 1) Ask the user to enter a number and print "even" or "odd " using conditional operator

number = int(input("enter a number for checking odd / even : "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd ")

# Question 2) Ask the user to enter a number and print "positive " or "negative".
number = float(input(" Enter a number to find out positive or negative :"))
if number > 0:
    print(f"{number} number is positive")

elif number == 0:
    print("number is equal to zero")
else:
    print(f"{number} is negative ")

# Question 3) Ask the user to enter two numbers and print the greater number

nums1 = float(input("enter first number : "))
nums2 = float(input("enter second number :"))
if nums1 > nums2:
    print(f"{nums1} : nums1 is grater ")
elif nums1 < nums2:
    print(f"{nums2} : nums2 is greater ")
else:
    print(f"nums1 and nums2 is equal")

# Question 4) Ask the user to enter two number and print the smaller number.
nums1 = float(input("enter first number :"))
nums2 = float(input("enter second number :"))
if (nums1 < nums2):
    print(f"{nums1} : nums1 is smaller than nums2")
elif (nums1 > nums2):
    print(f"{nums2} : nums2 is smaller than nums1")
else:
    print("nums1 and nums2 both are equal")

# Question 5) Ask the user to enter a number and check if it is zero or not.
number = int(input("enter a number :"))
if number == 0:
    print(f"number is equal to zero ")
else:
    print("number is not equal to zero")

# Question 6) Ask the user to enter age and print "eligible " or "not eligible" (voting >= 18).

age = int(input("enter your age : "))
if age >= 18:
    print(f"your age is {age} you are eligible for voting ")
else:
    print(f"you are not eligible for voting, you can vote after {18-age} years. ")

# Question 7) Ask the user to enter marks and print "pass" or "fail"(pass >= 40)
marks = int(input("enter your marks : "))
if marks >= 40 :
    print(f"{marks} is grater or equal to 40 so, pass")
else:
    marks < 40
    print(f"{marks} is less than 40 ")

# Question8) Ask the user to enter a number and print "greater than 10" or "less or equal to 10".

number = int(input("tell me your number : "))
if number > 10:
    print(f"{number} is greater than 10 ")
elif number < 10:
    print(f"{number} is less than 10 ")
else:
    print("number is equal to 10")

# Question 9) Ask the user to enter a number and print "divisible by 5" or "not divisible".
number = int(input("enter a number for checting number is divisible 5 or not : "))
if number % 5 == 0:
    print(f"{number} : is divisible by 5")
else:
    print(f"{number} : is not divisible by 5")

# Question 10) Ask the user to enter two numbers and check if they are equal or not.
nums1 = float(input("enter a first number :"))
nums2 = float(input("enter a second number :"))
if nums1 == nums2:
    print("nums1 = nums2 :both number are equal")
else:
    print("nums1 and nums2 are not equal ")


##   SHEET -- 8   IS COMPLETED
print(" SHEET --- 8 IS COPLETED ")