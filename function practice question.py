#.      practice set - 1.  (solve using function)

# Question 1) Ask the user to enter their name and print: welcome(Abhishek)!

# def greeting (name):
#     print(name)
# greeting("welcome abhishek")
# greeting("welcome rahul")
# greeting("welcome sheriyans")

#Question 2) Ask the user to enter their age and print : you are[age] years old.
# def info(age):
#     print(f"{age} years old")
# info(18)
# info(21)

# Question 3) Ask the user to enter their city and print : i live in[city].

# def details (city):
#     print(f"i live in city : {city} ")
# details("bhopal")
# details("ssm")

# # Question 4) Ask the user to enter their favorite color and print: my favourite color is [red].
# def info (colors):
#     print(f"my favourite colors is : {colors}")
# info("red")

# Question 5) Ask the user to enter their first name and last name saperately and print full name:

def full_name(first, last):
    """Concatenates and returns the full name."""
    return first + " " + last
first = input("enter first name")
last = input("enter last name :")  
print(first,last) 

# Question 6) check number is armstrong number or not using function
# def armstrong(n):
#     copy = n
#     sum = 0
#     length = len(str(n))
#     while n != 0:
#         ld = n % 10
#         sum = sum + ld ** length
#         n = n // 10
    
#     if copy == sum:
#         print("number is armstrong number")

#     else:
#         print("number is not armstrong number")

# armstrong(145)
# armstrong(153)

#  Question 7) Get information of employee

# def info(name, age, id = None):
#     print("info recieved")
# info("abhishek",24,234)

# Question 8) age checker using function

# def agechecker(n):
#     if n >= 18:
#         return True
#     else:
#         return False
# age = int(input("tell your age : "))

# if agechecker(age):
#     print("you can vote ")
# else:
#     print("you can not vote")

# Question 9)print 1 to 100 using function

# def numbers(n):
#     if n == 101:
#         return "done"
#     print(n)
#     numbers(n+1)
# numbers(1)

#Question 10) print reverse number 100 to 1

# def numbers(n):
#     if n == 0:
#         return "done"
#     print(n)
#     numbers(n - 1)
# numbers(101)

# or 

# def numbers(n):
#     if n == 101:
#         return "done"
#     numbers(n+1)
#     print(n)

# numbers(1)