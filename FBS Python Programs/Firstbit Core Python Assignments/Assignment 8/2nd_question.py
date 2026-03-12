# Write a program to calculate area of circle using Functions
import math

def calcArea(r):

    area = math.pi*r**2

    return area

radius = float(input("Enter radius of the circle: "))

ans = calcArea(radius)

print(f"The area of the circle is {ans:.2f} sq.units")