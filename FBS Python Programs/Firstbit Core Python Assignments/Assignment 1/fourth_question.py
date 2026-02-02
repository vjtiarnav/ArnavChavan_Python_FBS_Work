# Write a program to calculate Simple Interest

principal = int(input("Enter the principal amount: "))
rateOfInterest = float(input("Enter the rate of interest: "))
years = int(input("Enter the number of years: "))

simpleInterest = (principal*rateOfInterest*years)/100

print(f"The simple interest is {simpleInterest}")