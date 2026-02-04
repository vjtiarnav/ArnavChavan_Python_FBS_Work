# Write a program to check if user has entered correct userid and password.

correct_userID = 'test@gmail.com'
correct_password = 'test@123'

userID = input("Enter your User ID: ")
password = input("Enter the Password: ")

if(userID == correct_userID and password == correct_password):
    print("You have entered the correct credentials!!")
else:
    print("Invalid User ID or Password")