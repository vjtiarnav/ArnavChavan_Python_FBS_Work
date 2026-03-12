'''
Write a program to print Fibonacci series using recursion.
'''

def fibonacci(a,b,n):
    if(n!=0):
        c = a + b
        print(c)
        fibonacci(b,c,n-1)


n = int(input("Enter number of terms in your Fibonacci Series: "))
fibonacci(-1,1,n)
