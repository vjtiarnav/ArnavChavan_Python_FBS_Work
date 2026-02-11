#  WAP to check if given number is Perfect Number.
'''
A perfect number is a positive integer that is 
equal to the sum of its proper divisors, excluding itself.

Eg: Divisors of 28 are --> 1, 2, 4, 7, 14
    Sum of Divisors = 1 + 2 + 4 + 7 + 14
'''

# Using 'for' loop

n = int(input("Enter a number: "))
sumOfDivisors = 0 

for i in range(1,n):
    if(n % i == 0):
        sumOfDivisors += i
        
if(sumOfDivisors == n):
    print(f"{n} is a Perfect Number.")
else:
    print(f"{n} is not a Perfect Number.")


# Using 'while' loop

n = int(input("Enter a number: "))

if (n <= 0):
    print(f"{n} is not a Perfect Number")
    
else:
    
    i = 1
    sumOfDivisors = 0
    
    while(i < n):
        if n % i == 0:
            sumOfDivisors += i
        i += 1

    if (sumOfDivisors == n):
        print(f'{n} is a Perfect Number.')
    else:
        print(f'{n} is not a Perfect Number.')
    