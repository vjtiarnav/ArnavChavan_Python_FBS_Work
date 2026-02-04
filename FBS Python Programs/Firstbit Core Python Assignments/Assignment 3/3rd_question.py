# Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

angleSum = angle1 + angle2 + angle3

if(angleSum == 180):
    print("It is a valid triangle.")

else:
    print("It is not a valid triangle.")