# WAP to check if a given number is prime number or not.

# Using 'for' loop

n = int(input("Enter a number: "))

if n <= 1:
    print(f"{n} is not a prime number.")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")

        
# Using 'while' loop

n = int(input("Enter a number: "))
i = 2

if n <= 1:
    print(f"{n} is not a Prime Number.")
    
else:
    while i < n:
        if n % i == 0:
            print(f"{n} is not a Prime Number.")
            break
        i += 1
    
    else:
        print(f"{n} is a Prime Number.")