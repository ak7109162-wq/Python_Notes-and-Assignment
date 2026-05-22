# Question 1 ) Ask the user to enter a number and print all prime numbers up to that number.
n = int(input("enter your number :"))
for n in range(1,n+1):
    count = 0
    
    for i in range (1,n+1):
        if n % i == 0:
            count = count + 1

    if count > 2:
        print(f"composite nuber {n}")
    else:
        print(f"prime number {n}")

# Question 2) Ask the user to enter a number check if it is armstrong number

n = int(input("enter a number : "))
copy = n
length = len(str(n))
sum = 0
while n != 0:
    ld = n % 10
    sum = sum + ld ** length
    n = n // 10
if copy == sum:
    print("number is armstrong number")
else:
    print("number is not armstrong number")

# Question 3) Ask the user to enter a number and print the sum of digits using loop

n = int(input("enter a number : "))
sum = 0

while n != 0:
    ld = n % 10
    sum = sum + ld
    n = n//10

print(sum)


# Queestion 5) Ask the user to enter a number and check if it is palindrome 

n = int(input("enter a number : "))
copy = n
rev = 0
while n != 0:
    ld = n % 10
    rev = rev * 10 + ld
    n = n // 10

if copy == rev:
        print("number is palindrome")
else:
        print("print number is not palindrome ")

# QUestion 4) Ask the user to enter a number and print reverse of the number 

n = int(input("enter a number : "))
rev = 0
while n != 0:
       ld = n % 10
       rev = rev * 10 + ld
       n = n // 10
print(rev)

# # Question 6) Ask the user to enter a number and print all numbers between 1 to n thet are divisible by both 3 and 5.

n = int(input("Enter a number: "))
print(f"Numbers between 1 and {n} divisible by both 3 and 5:")
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# Question 7) Ask the user to enter a number and print factorial using loop using loop without using built- in function

n = int(input("enter a number : "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)

# or.  without using built in function

n = int(input("enter a number to findout factorial :"))
fact = 1

if n < 0:
    print("factoral doesn't exist !!")
elif n == 0:
    print("the factorial of zero is : 1")  

else:
    for i in range(1 , n+1):
        fact = fact * i 
print(fact)

print("sheet -- 11 is completed")
#.          SHEET -- 11(COMPLETED)