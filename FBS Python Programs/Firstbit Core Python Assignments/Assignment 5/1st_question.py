'''
Write a program to prompt user to enter userid and password. If ID and
password is incorrect give him chance to re-enter the credentials. 
Let him try 3 times. After that program to terminate.
'''
correct_userID = "test@gmail.com"
correct_password = "test@123"

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == correct_userID and password == correct_password:
    print("Successful Login!!")
else:
    attempts_left = 3
    while attempts_left > 0:
        print(f"Credentials are wrong. You have {attempts_left} attempt(s) left. Re-enter the credentials")
        userid = input("Enter User ID: ")
        password = input("Enter Password: ")

        if userid == correct_userID and password == correct_password:
            print("Successful Login!!")
            break
        
        attempts_left -= 1
    else:
        print("Program terminated")
