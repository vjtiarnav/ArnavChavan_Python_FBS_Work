# Write a program to check if entered year is a leap year or not.

def checkLeapYear(n):
    if(n % 4 == 0):
        if(n % 100 == 0):
            if(n % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
            
year = int(input("Enter a year: "))
isLeapYear = checkLeapYear(year)

if(isLeapYear):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")