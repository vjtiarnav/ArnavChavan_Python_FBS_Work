# Write a program to find sum of the following series using functions :
# 1!+ 2! + 3! + 4!+..... + n!

def sumOfSeries(n):
    total = 0
    for i in range(1,n+1):
        fact = 1
        for j in range(1,i+1):
            fact *= j
        
        total += fact

    return total
    

num = int(input("Enter a number: "))
ans = sumOfSeries(num)

print(f"The sum of series 1! + 2! + 3! + 4! + .....+ n! for n = {num} is {ans}")