# Find the area and circumference of a circle
import math

radius = float(input("Enter radius of the circle in cm: "))

area = math.pi*radius**2
circumference = 2*math.pi*radius

print(f"The area of the circle is {area} cm^2 and the circumference of the circle is {circumference} cm")