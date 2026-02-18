# Write a program to solve the following series: 
# S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter a number: "))

sumOfSeries = 0

for i in range(1, 11):
    sumOfSeries += (a ** i) / i

print(f"The sum of the series S = a + a^2/2 + a^3/3 + ... + a^10/10 for a = {a} is {sumOfSeries:.2f}")
