'''
Write a program to find factorial using recursion.
'''

def fact(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n*fact(n-1)
    
num = int(input("Enter a number: "))
ans = fact(num)
print(f"The factorial of {num} is {ans}")