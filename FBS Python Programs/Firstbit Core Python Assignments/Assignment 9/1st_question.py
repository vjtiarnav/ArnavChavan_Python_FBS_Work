'''
Write a program to find sum of following series using recursive functions:
1! + 2! + 3! + 4! +..... + n!
Note : For fact and sum two recursive functions

'''
def fact(n):
    if(n == 1):
        return 1
        
    else:
        return n*fact(n-1)
        
        
def sumOfFact(n):
    if(n == 1):
        return fact(1)
    else:
        return fact(n) + sumOfFact(n-1)
    
num = int(input("Enter a number: "))
result = sumOfFact(num)
print(f"The sum of the series 1! + 2! + 3! + 4! + ..... + n! for n = {num} is {result}")