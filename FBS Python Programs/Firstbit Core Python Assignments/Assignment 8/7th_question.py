# Write a program to find sum of digits of a number

def sumOfDigits(n):
    total = 0
    while(n > 0):
        digit = n % 10
        total += digit
        n = n // 10
    
    return total
    
num = int(input("Enter a number: "))
ans = sumOfDigits(num)
print(f"The sum of digits of {num} is {ans}")