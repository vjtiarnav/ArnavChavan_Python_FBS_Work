# Write a program to find the roots of a quadratic equation

import math 

a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant: "))

x1 = (-b+math.sqrt(b**2-(4*a*c)))/2*a
x2 = (-b-math.sqrt(b**2-(4*a*c)))/2*a

print(f"The roots of the quadratic equation are {x1} and {x2}")