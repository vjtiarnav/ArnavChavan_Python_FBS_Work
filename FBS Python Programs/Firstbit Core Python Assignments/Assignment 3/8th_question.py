'''
Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)
'''

import random

correct_userID = 'test@gmail.com'
correct_password = 'test@123'

userID = input("Enter your User ID: ")
password = input("Enter the Password: ")

if(userID == correct_userID and password == correct_password):
    num = random.randint(1000,9999)
    print(num)
    user_input = int(input("Enter the above captcha: "))
    if(user_input == num):
        print("Sucessful Login!!")
    else:
        print("Invalid Captcha.")
else:
    print("Invalid User ID or Password")