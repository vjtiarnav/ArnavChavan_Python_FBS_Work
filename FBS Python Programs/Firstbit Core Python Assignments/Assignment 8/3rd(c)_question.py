# Write a program to find sum of the following series using functions :
# 1^1+ 2^2 + 3^3 + 4^4+..... + n^n

def sumOfSeries(n):
    total = 0
    for i in range(1,n+1):
        total += i**i
        
    return total
        
num = int(input("Enter a number: "))
ans = sumOfSeries(num)

print(f"The sum of series 1^1+ 2^2 + 3^3 + 4^4+..... + n^n for n = {num} is {ans}")