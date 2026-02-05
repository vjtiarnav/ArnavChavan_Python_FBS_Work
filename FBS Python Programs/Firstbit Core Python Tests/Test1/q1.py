import math

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
radius = breadth / 2

perimeter = 2*length + breadth + (math.pi*radius)
area = length*breadth + (math.pi*radius**2)/2

print(f"The perimeter of the figure is: {perimeter:.2f}")
print(f"The area of the figure is: {area:.2f}")