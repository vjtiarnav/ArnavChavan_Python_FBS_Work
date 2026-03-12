# Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

def Fibonacci(n):
    a = 0
    b = 1
    print(1)
    for i in range(n-1):
        c = a + b
        print(c)
        a = b
        b = c

num = int(input("Enter a number: "))
print(f"The Fibonacci Series for the first {num} terms is: ")
Fibonacci(num)