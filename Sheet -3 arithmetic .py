# Question 1) Ask the user to enter two numbers and print their sum.

nums1 = int(input("Enter first number : "))
nums2 = int(input("enter second number : "))
sum = (nums1 + nums2 )
print(f"sum of two number is : {sum}")

# Question 2) Ask the user to enter two numbers and print their difference.

nums1 = int(input("enter first number : "))
nums2 = int(input("enter second number : "))
difference = (nums1 - nums2)
print(f"differnce is : {difference}")

# Question 3) Ask the user to enter two number and print their product

nums1 = int(input("enter first number to find product : "))
nums2 = int(input('enter second number to find product : '))
product =(nums1 * nums2)
print(f"product of two number is : {product}")

#Question 4) ask the user to enter two numbers and print their division.

nums1= float(input("enter first number for division : "))
nums2 = float(input("enter second number for divison : "))
division = nums1 / nums2
print(f"division is : {division}")
#float = 8/2 = 4.0
#int = 8/2 = 4

# Question 5) Ask the user to enter two numbers and print the remainder
nums1 = int(input("enter first number for finding remainder : "))
nums2 = int(input("enter second number for finding remainder : "))
remainder = (nums1 % nums2)
print("remainder is : {remainder}")

# question 6) Ask the user to enter two numbers and print the result of exponentiation
nums1 = int(input("Enter 1st number for find exponential :"))
nums2 = int(input("enter 2nd number for finding decimal : "))
exponentiation = (nums1 ** nums2)
print(f"exponention is : {exponentiation}")

# Question 7)Ask the user to enter two two numbers and print the floor division result
nums1 = float(input("enter first number : "))
nums2 = float(input("enter second number : "))
floordivision = nums1 // nums2
print(f"floor division result is : {floordivision}")

# Question 8) Ask the user to enter a number and print its square 
nums = int(input("enter a number : ")) 
square = nums ** 2
print(f"the square of number is {square}")

# Question 9) Ask the user to enter a number and print its cube
nums = int(input("enter the number :"))
cube = nums ** 3
print(f"cube of the number is : {cube}")

# Question 10)Ask the user to enter two numbers and print all operations (sum, difference, product, division).

nums1 = int(input("enter first number : "))
nums2 = int(input("enter second number : "))
sum = nums1 + nums2
difference = nums1 - nums2
product = nums1 * nums2
division = float(nums1 / nums2)

print(f"sum of two number is :{sum} and difference of two number is {difference} ,product of two number is {product} and division is : {division} ")