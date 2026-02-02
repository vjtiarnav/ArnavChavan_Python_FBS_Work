# Convert temp from Celsius into Fahrenheit 

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (9/5)*celsius + 32
fahrenheit = round(fahrenheit,2)

print(f"{celsius} °C is {fahrenheit} °F")