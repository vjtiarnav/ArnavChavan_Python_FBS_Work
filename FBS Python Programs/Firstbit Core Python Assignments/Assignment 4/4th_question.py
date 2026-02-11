# WAP to print factorial of a number.

# Using 'for' loop

n = int(input("Enter a number: "))
fact = 1

for i in range(1,n+1):
    fact *= i

print(f"The factorial of {n} is {fact}")

# Using 'while' loop

n = int(input("Enter a number: "))
i = 1
fact = 1
while (i <= n):
    fact *= i
    i += 1

print(f"The factorial of {n} is {fact}")