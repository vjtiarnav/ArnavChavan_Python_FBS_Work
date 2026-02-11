# WAP to check if given number is a Strong Number.

# Using 'for' loop

n = int(input("Enter a number: "))
original = n
sum_of_factorials = 0

for digit_char in str(n):
    digit = int(digit_char)
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum_of_factorials += fact

if sum_of_factorials == original:
    print(f"{original} is a Strong Number.")
else:
    print(f"{original} is not a Strong Number.")


# Using 'while' loop

# Method 1
isnotStrong = True

while(isnotStrong):
    n = int(input("Enter a number: "))
    originalNum = n
    sumofFact = 0
    
    while(n > 0):
        digit = n % 10
        fact = 1
        for i in range(1,digit+1):
            fact *= i
        sumofFact += fact
        n = n // 10
        
    if(sumofFact == originalNum):
        print(f"{originalNum} is a Strong Number")
        isnotStrong = False
    else:
        print(f"{originalNum} is not a Strong Number\n")
        

# Method 2
n = int(input("Enter a number: "))
original = n
sum_of_factorials = 0

while n > 0:
    digit = n % 10
    # Calculate factorial of the digit
    fact = 1
    i = 1
    while i <= digit:
        fact *= i
        i += 1
    sum_of_factorials += fact
    n //= 10

if sum_of_factorials == original:
    print(f"{original} is a Strong Number.")
else:
    print(f"{original} is not a Strong Number.")