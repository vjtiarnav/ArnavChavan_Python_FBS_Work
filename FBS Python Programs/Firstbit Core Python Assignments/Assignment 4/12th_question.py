# Write a program to check if given number is Armstrong number or not.

# Using 'for' loop

n = int(input("Enter a number: "))
original = n

digits = len(str(n))

sum_of_digits = 0

for i in range(digits):
    digit = n % 10
    sum_of_digits += digit**digits
    n = n // 10
    
if (sum_of_digits == original):
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")

    
# Using 'while' loop

n = int(input("Enter a number: "))
original = n

sumOfDigits = 0
digits = 0

while(n > 0):
    digits += 1
    n = n // 10
    
n = original

while(n > 0):
    digit = n % 10
    sumOfDigits += digit**digits
    n = n // 10
    
if (sumOfDigits == original):
    print(f"{original} is an Armstrong Number.")
else:
    print(f"{original} is not an Armstrong Number.")