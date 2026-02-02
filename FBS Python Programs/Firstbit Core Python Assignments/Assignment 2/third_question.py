# Convert distance given in feet and inches into meter and centimeter

# Input from user
feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

# Convert feet and inches to total inches
total_inches = feet * 12 + inches

# Convert inches to centimeters
total_cm = total_inches * 2.54

# Convert centimeters to meters and remaining centimeters
meters = int(total_cm // 100)
centimeters = total_cm % 100

# Output the result
print(f"{feet} feet and {inches} inches is equal to {meters} meters and {centimeters:.2f} centimeters.")
