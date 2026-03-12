'''
Write a program to find sum of digits using recursion.
'''
def sumOfDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumOfDigits(n // 10)
    
num = int(input("Enter a number: "))
ans = sumOfDigits(num)
print(f"The sum of digits of {num} is {ans}")