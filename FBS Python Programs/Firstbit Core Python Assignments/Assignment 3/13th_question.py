'''
Write a program to input electricity unit charges and calculate total electricity bill
according to the given condition:
    For first 50 units Rs. 0.50/unit
    For next 100 units Rs. 0.75/unit
    For next 100 units Rs. 1.20/unit
    For unit above 250 Rs. 1.50/unit
    An additional surcharge of 20% is added to the bill
'''
#Method 1

units = float(input("Enter the number of units consumed: "))

if units <= 50:
    bill = units * 0.5

elif units <= 150:
    bill = 50 * 0.5
    bill += (units - 50) * 0.75

elif units <= 250:
    bill = 50 * 0.5
    bill += 100 * 0.75
    bill += (units - 150) * 1.20

else:
    bill = 50 * 0.5
    bill += 100 * 0.75
    bill += 100 * 1.20
    bill += (units - 250) * 1.50

# Add 20% surcharge
bill += bill * 0.20

print(f"The bill is Rs.{bill:.2f}")


# Method 2

units = float(input("Enter the number of units of electricity consumed:"))
amount = 0

if units <= 50:
    amount = amount + (0.5*units)
elif units > 50 and units <= 150:
    amount = amount + (0.5*50) + (0.75*(units-50))
elif units > 150 and units <= 250:
    amount = amount + (0.5*50) + (0.75*100) + (1.2*(units-150))
elif units > 250:
    amount = amount + (0.5*50) + (0.75*100) + (1.2*100) + (1.5*(units-250))

total = 1.2*amount
print(f"The total bill is {total:.2f}")


# Method 3 (Most Optimized Method)

units = float(input("Enter the number of units of electricity consumed: "))
amount = 0

# Calculate units in each slab
unit_50 = min(units, 50)
unit_100_1 = min(max(units - 50, 0), 100)
unit_100_2 = min(max(units - 150, 0), 100)
unit_above_250 = max(units - 250, 0)

# Calculate amount
amount = (
    unit_50 * 0.5 +
    unit_100_1 * 0.75 +
    unit_100_2 * 1.2 +
    unit_above_250 * 1.5
)

# Add 20% surcharge
total = amount * 1.2

print(f"The total bill is {total:.2f}")
