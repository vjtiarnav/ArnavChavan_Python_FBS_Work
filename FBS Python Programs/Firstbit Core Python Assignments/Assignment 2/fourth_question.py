# WAP to calculate area of triangle and rectangle

print("Calculate Area of Triangle")
base = float(input("Enter the base of the triangle (in cm): "))
height = float(input("Enter the height of the triangle (in cm): "))
triangle_area = 0.5 * base * height
print(f"Area of the triangle is {triangle_area:.2f} square cm\n")

print("Calculate Area of Rectangle")
length = float(input("Enter the length of the rectangle (in cm): "))
width = float(input("Enter the width of the rectangle (in cm): "))
rectangle_area = length * width
print(f"Area of the rectangle is {rectangle_area:.2f} square cm")
