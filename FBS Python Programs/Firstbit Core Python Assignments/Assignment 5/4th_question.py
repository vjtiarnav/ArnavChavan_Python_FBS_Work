# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3)

num = int(input("Enter a number: "))
temp = num

count = 0
sumOfDigits = 0

# Counting number of digits
while(temp > 0):
    count += 1
    temp = temp // 10

#Checking if num is Armstrong number or not
temp = num
while(temp > 0):
    digit = temp % 10
    sumOfDigits += digit**count
    temp = temp // 10

if(sumOfDigits == num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
