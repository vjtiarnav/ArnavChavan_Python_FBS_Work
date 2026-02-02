''' 
WAP to calculate the total salary of an employee based on basic, 
da = 10% of basic, ta = 12% of basic, hra = 15% of basic
'''

basic = int(input("Enter the basic salary: "))

da = 0.1*basic
ta = 0.12*basic
hra = 0.15*basic

totalSalary = basic + da + ta + hra

print(f"The total salary of the employee is Rs.{totalSalary}")