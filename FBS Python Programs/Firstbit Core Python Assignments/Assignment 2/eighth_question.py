# Write a program to swap two numbers using third variable

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Before swapping num1 = {num1} and num2 = {num2}")

temp = num1
num1 = num2
num2 = temp

print(f"After swapping num1 = {num1} and num2 = {num2}")