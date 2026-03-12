'''
Write a program to calculate the m to the power n using recursion.
'''

def power(m,n):
    
    if(n == 0):
        return 1
    
    elif(n == 1):
        return m
    
    else:
        return m*power(m,n-1)
        
m = int(input("Enter a number: "))
n = int(input("Enter the power: "))
ans = power(m,n)

print(f"{m} raised to {n} is {ans}")