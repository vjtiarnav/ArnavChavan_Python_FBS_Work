'''
Write a program to find sum of n numbers using recursion.
'''

def sumOfNums(n):
    if(n == 1):
        return 1
    else:
        return n + sumOfNums(n-1)

num = int(input("Enter a number: "))
result = sumOfNums(num)
print(f"The sum of numbers from 1 to {num} is {result}")