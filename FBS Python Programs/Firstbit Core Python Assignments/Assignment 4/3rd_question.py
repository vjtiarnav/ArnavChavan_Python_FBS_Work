# WAP to print sum of series upto n.

#Using 'for' loop

n = int(input("Enter a number: "))
sumOfNumbers = 0

for i in range(1,n+1):
    sumOfNumbers += i

print(f"The sum of numbers from 1 to {n} is {sumOfNumbers}")

#Using 'while' loop

n = int(input("Enter a number: "))
i = 1
sumOfSeries = 0
while(i <= n):
    sumOfSeries += i
    i += 1

print(f"The sum of numbers from 1 to {n} is {sumOfSeries}")
