# WAP to print Fibonacci series upto n.

# Using 'for' loop

n = int(input("Enter the number of terms you want in Fibonacci series: "))
a = -1
b = 1

for i in range(n):
    c = a + b
    print(c)
    a = b
    b = c

# Using 'while' loop

n = int(input("Enter number of terms in Fibonacci Series: "))
a = -1
b = 1
i = 1
while (i <= n):
    c = a + b
    print(c)
    a = b
    b = c
    i += 1