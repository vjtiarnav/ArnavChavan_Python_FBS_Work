# Write a program to find quotient and remainder of two numbers

dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

quotient  = dividend // divisor
remainder = dividend % divisor

print(f"The quotient is {quotient} and the remainder is {remainder}")