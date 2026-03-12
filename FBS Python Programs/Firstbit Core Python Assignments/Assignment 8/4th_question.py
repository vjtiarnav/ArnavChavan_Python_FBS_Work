# Sum of all odd numbers between 1 to n

def sumOfOddNums(n):
    total = 0
    for i in range(1,n+1):
        if(i % 2 != 0):
            total += i

    return total

num = int(input("Enter a number: "))
ans = sumOfOddNums(num)

print(f"The sum of all odd numbers between 1 to {num} is {ans}")