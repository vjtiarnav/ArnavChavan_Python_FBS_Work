'''
Write a program to reverse a number using recursion.
'''
def reverseNum(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverseNum(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))
ans = reverseNum(num)
print(f"The reverse of {num} is {ans}")