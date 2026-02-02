# Write a program to swap two numbers without using third variable

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Before swapping num1 = {num1} and num2 = {num2}")

num1, num2 = num2, num1
print(f"After swapping num1 = {num1} and num2 = {num2}")

# Alternate Method
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2