# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

# Using 'for' loop

start = int(input("Enter the start value of the range: "))
end = int(input("Enter the end value of the range: "))

for i in range(start,end+1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end = " ")


# Using 'while' loop

start = int(input("Enter the start value of the range: "))
end = int(input("Enter the end value of the range: "))

i = start
while(i <= end):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end = " ")
    i += 1