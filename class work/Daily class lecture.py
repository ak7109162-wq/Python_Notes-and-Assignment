# comparision operator
#(== , > , < , >= , <= , !=)
# these operators wil compare between two things
# and they will always produce result in boolean

print(12 <= 12)
print(12.1 != 12)

# logical operator
# (and , or ,not)

# "and" operator

print(12 == 12 and 56==56 and 34>78 and 12 >10) # false
# All the operation must be true 
# if a single operator is false the final result is also
# going to be false

# "or" operator
print(12 > 34 or 13==45 or 56==78 or 12==12) # true
# if one of operator is true 
# the whole result will be true

# "not" operator
print(not 12 == 12)
# it convert true to false and false to true

print(bool(0) and 12==12) # false





##  Topic -  control flow
# (if else ,loops , functions )

age = int(input("apni age bata : "))

if age >= 18:
    print("you can vote")

else:
    print("you cannot vote ")


#Question) accept two number and print the gratest between them (if , elif ,else question)

a = int(input("tell your first number "))
b = int(input("enter second number "))

if a > b:
    print("a is greater than b")

elif b > a:
    print("b is greater than a")
else:
    print("both are equal")

# Question 2) accept the gender from the user

gen = input("please tell your gender as char (M or F)")
if gen == "M" or gen == "m":
    print("good morning sir ")
elif gen == "F" or gen == "f":
    print("good morning mam")
else:
    print("unknown gender")

#Question 3) Accept the number from user and find number is odd or even

a = int(input("plesae tell your number"))

if a % 2 == 0:
    print("your number is even")

else:
    print("your number is odd ")


# Question 4)
name = input("please tell your name :")
age = int(input("please tell your age :"))

if age >= 18:
    print(f"hello {name} you are a valid voter")

else:
    print(f"hello {name} you are not voter you can voter after {18 - age} years")
    


# check number is lies between 10 & 50
num = int(input("tell your number : "))
if num >= 10 and num <= 50:
    print("your numberus between 10 and 50")
else:
    print("your number is out of range")

# Question) A student passed if they score  >= 40 int both math & english , or score >= 80 at least

m = int(input("tell your score in maths : "))
e = int(input("tell your score in english :"))

if m >= 40 and e >= 40:
    print("you passed")
elif m >= 80 or e >= 80:
    print("you passed")
else:
    print("you failed ")


# Quection ) check if a chraacter is vowel or not
ch = input("please tell your charaxter : -")
if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print("its a vowel")
else:
    print("consonant")
      
      # or
ch = input("please tell your charaxter : -")

if ch in "AEIOUaeiou":
    print("its a vowel")

else:
    print("its a consonent")

# question ) check a year is a leap year

year = int(input ("plese tell your year : "))

if year % 100 == 0 and year % 400 == 0:
    print("your year is a leap year ")
elif year % 100 != 0 and year % 4 == 0:
    print("your year is a leap year ")
else:
    print("its a normal year")


# A number is a special number if it id divisible by 3 and 5 , or divisible by 7 but not by 10.
num = int(input ( " tell your number :"))

if num % 3 == 0 and num % 5 == 0:
    print("number is special")

elif num % 7 == 0 and num % 10 != 0:
    print("special number")

else:
    print(" not special")


