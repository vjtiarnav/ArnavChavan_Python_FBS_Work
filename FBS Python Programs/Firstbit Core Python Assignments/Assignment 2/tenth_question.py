# Write a program to reverse three-digit number

num = int(input("Enter a three digit number: "))

temp = num # Using a temporary variable so that original num is not changed
a = temp % 10
temp = temp // 10
b = temp % 10
c = temp // 10

reversedNum = (a*100)+(b*10)+c

print(f"Entered number is {num}")
print(f"The reversed number is {reversedNum}")