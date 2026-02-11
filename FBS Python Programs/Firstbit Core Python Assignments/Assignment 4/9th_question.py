# WAP to print all numbers in a range divisible by a given number.

# Using 'for' loop

start = int(input("Enter the start value of the range: "))
end = int(input("Enter the end value of the range: "))

num = int(input("Enter a number: "))

print(f"\nThe numbers from {start} to {end} that are divisible by {num} are:")
for n in range(start,end+1):
    if (n % num == 0):
        print(n)

# Using 'while' loop

start = int(input("Enter the start value of the range: "))
end = int(input("Enter the end value of the range: "))

num = int(input("Enter a number: "))

i = start

while(i <= end):
    if (i % num == 0):
        print(i)
    i += 1