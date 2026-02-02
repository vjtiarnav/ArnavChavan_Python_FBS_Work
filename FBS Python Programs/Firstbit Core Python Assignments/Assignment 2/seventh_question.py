# Find the sum of digits of a 3-digit number

num = int(input("Enter a three digit number: "))

a = num % 10
num = num // 10
b = num % 10
c = num // 10

sumOfDigits = a + b + c

print(f"The sum of the digits of {num} is {sumOfDigits}")