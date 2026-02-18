'''
Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount of ticket to travel for all of them based 
on following condition :
    a. Children below 12 = 30% discount
    b. Senior citizen (above 59) = 50% discount
    c. Others need to pay full.
'''
num_passengers = int(input("Enter the number of passengers: "))
cost_per_ticket = float(input("Enter the cost per ticket: "))

total_cost = 0

for i in range(num_passengers):
    age = int(input(f"Enter the age of Passenger {i+1}: "))

    if(age < 12):
        total_cost += (cost_per_ticket*0.7)

    elif(age > 59):
        total_cost += (cost_per_ticket*0.5)

    else:
        total_cost += cost_per_ticket

print(f"The total amount of ticket to travel for all {num_passengers} is Rs.{total_cost:.2f}")


