# Write a program to input two angles from the user and find the third angle of the triangle

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))

angle3 = 180 - (angle1+angle2)

print(f"The third angle of the triangle is {angle3}")