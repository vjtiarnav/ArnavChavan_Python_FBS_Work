'''
Write a program to check whether a number is prime or not using recursion.
'''
def isPrime(num, i=2):
    #Base cases
    if(num <= 2):
        return True if num == 2 else False
    if(num % i == 0):
        return False
    if(i == num-1):
        return True
    
    isPrime(num, i+1)

num = int(input("Enter a number: "))

if isPrime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")