# Write a program to print first n prime numbers

n = int(input("Enter how many prime numbers you want: "))

count = 0
num = 2

while count < n:
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    if i == num:
        print(num, end=' ')
        count += 1
    num += 1

# 'count' keeps track of how many prime numbers have been found so far.
# 'num' is the current number being checked to see if it's prime.
# For each 'num', we check divisibility using 'i', starting from 2 up to num-1.
# If 'num' is not divisible by any 'i', then 'num' is prime.
# We print the prime number and increase 'count' until we reach 'n' primes.