# Write a program to solve the following series: 
# x - x2/3 + x3/5 - x4/7 + .... to n terms

n = int(input("Enter number of terms: "))
x = int(input("Enter a number: "))

sum_of_series = 0
for i in range(1,n+1):
    if(i % 2 == 0):
        sum_of_series -= x**i/(2*i-1)
    else:
        sum_of_series += x**i/(2*i-1)
        
print(f"The sum of series x - x^2/3 + x^3/5 - x^4/7 + .... to {n} terms is {sum_of_series:.2f}")