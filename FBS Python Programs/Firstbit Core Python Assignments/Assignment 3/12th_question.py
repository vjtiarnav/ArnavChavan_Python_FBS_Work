# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a three digit number: "))
originalNum = num 

reversedNum = 0
while(num>0):
    digit = num % 10
    reversedNum = (reversedNum*10) + digit
    num = num // 10

print(f"The reversed number is {reversedNum}")

if(reversedNum == originalNum):
    print(f"{originalNum} is a palindrome number.")
else:
    print(f"{originalNum} is not a palindrome number.")