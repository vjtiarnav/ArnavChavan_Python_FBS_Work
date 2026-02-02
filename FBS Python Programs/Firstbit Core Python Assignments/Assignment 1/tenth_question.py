# Write a program to calculate area of an equilateral triangle
import math

side = float(input("Enter the length of the side of an equilateral triangle: "))

area = (math.sqrt(3)/4)*side**2

print(f"The area of the equilateral triangle is {area}")