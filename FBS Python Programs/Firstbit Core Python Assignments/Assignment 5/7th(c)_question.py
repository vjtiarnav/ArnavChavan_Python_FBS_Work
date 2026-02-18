# Write a program to solve the following series: 
# Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter the number of terms: "))
common_ratio = 2
sum_of_series = (common_ratio)**n - 1
print(f"The sum of the geometric series 1 + 2 + 4 + ... to {n} terms is {sum_of_series}")
