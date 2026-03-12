# Sum of all prime numbers between 1 to n

def sumOfPrimeNums(n):
    total = 0
    for i in range(2,n+1):
        
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            total += i

    return total

num = int(input("Enter a number: "))
ans = sumOfPrimeNums(num)

print(f"The sum of all prime numbers between 1 to {num} is {ans}")