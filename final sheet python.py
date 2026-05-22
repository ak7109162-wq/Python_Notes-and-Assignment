#               Question based on --> "string"

# Question 31) print string in reverse ,its length ,in uppercase, lowercase and copy into another string

# s = "i am writing code in python"
# print(f"reverse string : {s[::-1]}")
# print(f"length of string :{len(s)}")
# print(f"upper case of string : {s.upper()}")
# print(f"lower case of string : {s.lower()}")

#Question 32) Arrange string characters such that lowercae letters shuld come first

# s = "ShEry"
# lower = " "
# upper = " "
# for i in s:
#     if i.islower():
#         lower = lower + i

#     elif i.isupper():
#         upper = upper + i

# print(lower + upper)

#Question 33) count all letters ,digits, and special symbols from a given string

# str1 = "P@#yn26at^&i5ve"
# alpha = 0
# digit = 0
# special = 0
# for i in str1:
#     if i.isalpha():
#         alpha = alpha + 1
#     elif i.isdigit():
#         digit = digit + 1
#     else:
        # special = special + 1
# print(f"total no of alphabet : {alpha}")
# print(f"total number of digit : {digit}")
# print(f"total number of special char : {special}")

# Question 34) compare two string without using functions
# str1 = "Hello"
# str2 = "hello"
# if len(str1) == len(str2):
#    print("length of both string are same")
#    for i in range(len(str1)):
#        if str1[i] != str2[i]:
#           print("indexing value of string are not same ")
#           break
#        else:
#            print("indexing value of string are same")
# else:
#     print("length of both string are not the same length")

# Question 35) count vowel from given string

# char = "Hello i am Abhishek .it's pleasure to meet you "
# count = 0
# vowel = "aeiouAEIOU"
# for i in char:
#     if i in vowel:
#         count = count + 1
# print(f"numbers of vowels: {count}" )

# Question 36) Reverse a string
# s = input("enter a string :")
# print(f"reverse string is : {s[::-1]}")

#Question 37) check string is paindrome or not

# str1 = input("enter a string :")
# rev = (str1[::-1])
# if rev == str1:
#     print("string is palindrome ")
# else:
#     print("string is not palindrome")

#  OR  check number is palindrome or not

# n = int(input("enter a number : "))
# copy = n 
# rev = 0

# while n != 0:
#     ld = n % 10
#     rev = rev * 10 + ld
#     n = n // 10
# if rev == copy:
#     print("number is  palindrome")
# else:
#     print("number is not palindrome ")


                        # QUESTION -- > 16) 

# Accept an integer and print hello world n times

# n = int(input("enter a number to how many times to print string : "))
# print("hello world \n" * n)

#          OR (solve by using for loop)
# n = int(input("enter a number : "))
# for i in range(n):
    # print("hello world")

#          OR (solve by using while loop)
# n = int(input("Enter a number: "))
# count = 0
# while count != n:
#     print("Hello World")
#     count += 1

#.        OR (solve by function)
# def printhello():
#     n = int(input("enter a number : "))
#     count = 0
#     while count != n:
#         print("Hello i am Abhishek")
#         count += 1
#     return f"{count}"
# print(printhello())

        
           # QUESTION --> 17) 
# Print natural number up to n:

#       solve by (for loop)
# # n = int(input("enter a number upto print natural number : "))
# # for i in range(1,n+1):
# #     print(i)

# #        OR (solve by while loop)
# n = int(input("enter a number upto print natural number : "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1

#   OR (solve by recursion function )
# def naturalnumber():
#     n = int(input("enter a number upto print natural number : "))
#     i = 1
#     while i <= n:
#         print(i)
#         i += 1
#     return f"{i}"
# print(naturalnumber())

#          QUESTION==> 18)
# Reverse for loop. print n to 1.
# n = input("enter a number : ")
# print(n[::-1])

# [OR]  using (for loop) reverse number 
# n = input("enter your digit : ")
# digit = " "
# for i in str(n)[::-1]:
#     digit = digit + i
# print(digit)

# [OR] solve by using (while loop )
# n = int(input("enter a number : "))
# rev = 0
# while n > 0:
#     ld = n % 10
#     rev = rev * 10 + ld
#     n = n // 10
# print(rev)

# [OR] solve by using (function)
# def rev_number(n):
#     rev = 0
#     while n > 0:
#         ld = n % 10
#         rev = rev * 10 + ld
#         n = n // 10
#     return f"reverse number is : {rev}"
# print(rev_number(124))
# print(rev_number(9852))

#.            QUESTION==> 19)
# Take a number as input and print its table .

# n = int(input("enter a number : "))

# for i in range(1,11):
#     print(f"{n} x {i} = {n * i}")

# [OR] print table using (while loop )

# n = int(input("enter a number : "))
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n * i}")
#     i = i + 1
# [OR] print table using recursion(function)

# def print_table(n):
#     i = 1
#     while i <= 10:
#         print(f"{n} x {i} = {n * i}")
#         i = i+1
# print(print_table(5))
# print(print_table(6))
    
#.           QUESTION ==> 20)

# sum up to n terms.
# [solve by for loop]
# n = int(input("enter a number upto want to print sum :"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

#[OR] solve by formula
# n = int(input("enter a number : "))
# sum = n*(n+1)//2
# print(f"sum of n natural number : {sum}")

#[OR] solve by using while loop
# n = int(input("enter a number : "))
# i = 1
# sum = 0
# while i <= n:
#     sum = sum + i
#     i += 1
# print(sum)

# [OR] SOLVE BY USING (FUNCTION)
# def sum(n: int):
#     i = 1
#     sum = 0
#     while i <= n:
#         sum = sum + i
#         i += 1
#     return f"sum of n terms number {n} is : {sum}"
# print(sum(3))
# print(sum(4))
# print(sum(5))


#                   QUESTION ==> 21)
# Find factorial of a number [solving by for loop]

# n = int(input("enter a number : "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

#[OR] find factorial using [while loop]

# n = int(input("enter a number : "))
# i = 1
# fact = 1
# while i <= n:
#     fact = fact * i
#     i += 1
# print(fact)

#[OR] find factorial using [recursion function]

# def print_factorial(n):
#     # n = int(input("enter a number : "))
#     i = 1 
#     fact = 1
#     while i <= n:
#         fact = fact * i 
#         i += 1
#     return f"factorial of number : {fact}"
# print(print_factorial(3))


#              QUESTION ==> 22)
# print the sum of all even and odd in a range seperately{ by if - else statement}
# n = int(input("enter a number : "))
# if n % 2 == 0:
#     print("number is even ")
# else:
#     print("number is odd")

#[OR] find odd or even using for loop
# n = int(input("enter a number : "))
# evensum = 0
# oddsum = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         evensum = evensum + i
#     else:
#         oddsum = oddsum + i
# print(f"even sum is : {evensum} and odd sum is : {oddsum}")

#[OR] print odd or even using while loop
n = int(input("enter a number : "))
i = 1
evensum = 0
oddsum = 0
while n <= i:
    if i % 2 == 0:
        i = i + 1
        print("even")
    else:
        print("odd")
        # i = i + 1

    



