# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter your gender (male/female): ").strip().lower()
age = int(input("Enter your age: "))

if gender == "male":
    if age >= 21:
        print("You are eligible to marry.")
    else:
        print("You are not eligible to marry. Minimum age for males is 21.")
elif gender == "female":
    if age >= 18:
        print("You are eligible to marry.")
    else:
        print("You are not eligible to marry. Minimum age for females is 18.")
else:
    print("Invalid gender entered. Please enter 'male' or 'female'.")
