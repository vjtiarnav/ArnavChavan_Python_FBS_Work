# Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1 = int(input("Enter the length of first side of the triangle: "))
side2 = int(input("Enter the length of second side of the triangle: "))
side3 = int(input("Enter the length of third side of the triangle: "))

if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    print("It is a valid triangle.")

else:
    print("It is not a valid triangle.")