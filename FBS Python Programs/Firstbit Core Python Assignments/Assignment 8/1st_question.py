# Write a program to calculate area of rectangle using Functions

def calcArea(l,b):

    area = l*b

    return area

length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))

ans = calcArea(length,breadth)

print(f"The area of the rectangle is {ans:.2f} sq.units")