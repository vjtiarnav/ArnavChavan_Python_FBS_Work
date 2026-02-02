# Write a program to convert days into years, weeks and days


total_days = int(input("Enter the number of days: "))

years = total_days // 365
remaining_days = total_days % 365
weeks = remaining_days // 7
days = remaining_days % 7

print(f"{total_days} days is approximately:")
print(f"{years} year(s), {weeks} week(s), and {days} day(s)")
