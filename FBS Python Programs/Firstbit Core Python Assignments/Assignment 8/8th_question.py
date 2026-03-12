# Write a program to find reverse of a number

def reverseNum(num):
    n = 0
    while(num > 0):
        digit = num % 10
        n = (n*10) + digit
        num = num // 10

    return n

num = int(input("Enter a number: "))
ans = reverseNum(num)

print(f"The reverse of {num} is {ans}")