# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1 = int(input("Enter the length of the first side of the triangle: "))
side2 = int(input("Enter the length of the second side of the triangle: "))
side3 = int(input("Enter the length of the third side of the triangle: "))

if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    if(side1 == side2 and side2 == side3):
        print("It is an Equilateral Triangle.")
    elif(side1 == side2 or side2 == side3 or side1 == side3):
        print("It is an Isosceles Triangle.")
    else:
        print("It is a Scalene Triangle.")
else:
    print("The given sides do not form a valid triangle.")

