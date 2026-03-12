# Write a program to check if entered number is a palindrome or not.

def isPalindrome(num):
    originalNum = num
    n = 0
    while(num > 0):
        digit = num % 10
        n = (n*10) + digit
        num = num // 10

    if(n == originalNum):
        return 'a Palindrome Number'
    else:
        return 'not a Palindrome Number'
    
number = int(input("Enter a number: "))
ans = isPalindrome(number)

print(f"{number} is {ans}")