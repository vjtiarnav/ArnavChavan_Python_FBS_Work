p = float(input("Enter Principal Amount: "))
r = float(input("Enter the Rate of Interest: "))
t = int(input("Enter time (in years): " ))

s_i = (p*r*t)/100

print(f"The Simple Interest for given data is {s_i:.2f}")