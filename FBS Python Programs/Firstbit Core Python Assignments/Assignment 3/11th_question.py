'''
Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
    a. Children below 12 = 30% discount
    b. Senior citizen (above 59) = 50% discount
    c. Others need to pay full.
'''

num = int(input("Enter the number of passengers: "))

passengers = []
fare = 1000
totalFare = 0

for i in range(num):
    age = int(input(f"Enter the age of passenger {i+1}: "))
    passengers.append(age)

for age in passengers:
    if(age <= 12):
        amount = 0.7*fare
    elif(12 <= age < 59):
        amount = fare
    else:
        amount = 0.5*fare
    
    totalFare = totalFare + amount

print(f"The total fare is Rs.{totalFare}")