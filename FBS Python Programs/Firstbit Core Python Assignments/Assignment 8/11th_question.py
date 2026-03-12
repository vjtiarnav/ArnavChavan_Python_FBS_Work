# Write a program to check if a given number is Armstrong number or not. 
# For each task create separate functions.

def countDigits(n):
    temp = n
    count = 0
    while(temp):
        temp = temp // 10
        count += 1
    
    return count
    
def sumOfDigits(n):
    temp = n
    
    num_of_digits = countDigits(n)
    
    total = 0
    while(temp > 0):
        digit = temp % 10
        total += digit**num_of_digits
        temp = temp // 10
        
    return total
    
def isArmstrong(n):
    
    ans = sumOfDigits(n)
    
    if(ans == n):
        return True
    else:
        return False
        
n = int(input("Enter a number: "))

if(isArmstrong(n)):
    print(f"{n} is an Armstrong number")
    
else:
    print(f"{n} is not an Armstrong number")
    
    