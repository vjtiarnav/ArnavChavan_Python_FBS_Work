# WAP to print all odd numbers until n.

#Using 'for' loop

n = int(input("Enter a number: "))

for i in range(1,n+1):
    if(i % 2 != 0):
        print(i)


# Using 'while' loop
n = int(input("Enter a number: "))
i = 1
while(i <= n):
    if i % 2 != 0:
        print(i)
    i += 1