'''
Write a program to check if given number is Armstrong or not using recursive function.
'''
def count(num):
    if(num != 0):
        return 1 + count(num // 10)
    else:
        return 0
    
def armstrong(num,c):
    if(num != 0):
        a = num % 10
        return a**c + armstrong(num // 10, c)
    else:
        return 0  
    
num = int(input("Enter a number: "))
c = count(num)
ans = armstrong(num,c)

if(ans == num):
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")