# WAP to print all integers upto n that aren’t divisible by 2 and 3.

# Using 'for' loop

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=' ')

# Using 'while' loop

n = int(input("Enter a number: "))
i = 1

while (i <= n):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end = ' ')
    
    i += 1