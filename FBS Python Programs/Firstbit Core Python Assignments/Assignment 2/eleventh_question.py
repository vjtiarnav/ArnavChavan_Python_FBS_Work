amount = int(input("Enter an integer amount: "))

notesOf500 = amount // 500 
remainingAmount = amount % 500
notesOf200 = remainingAmount // 200
remainingAmount = remainingAmount % 200
notesOf100 = remainingAmount // 100
remainingAmount = remainingAmount % 100
notesOf50 = remainingAmount // 50
remainingAmount = remainingAmount % 50
notesOf20 = remainingAmount // 20
remainingAmount = remainingAmount % 20
notesOf10 = remainingAmount // 10
remainingAmount = remainingAmount % 10

print(f"\nNumber of notes of Rs.500 is {notesOf500}")
print(f"Number of notes of Rs.200 is {notesOf200}")
print(f"Number of notes of Rs.100 is {notesOf100}")
print(f"Number of notes of Rs.50 is {notesOf50}")
print(f"Number of notes of Rs.20 is {notesOf20}")
print(f"Number of notes of Rs.10 is {notesOf10}")

minNotes = notesOf500+notesOf200+notesOf100+notesOf50+notesOf20+notesOf10

print(f"\n The minimum number of notes needed for representing Rs. {amount} is {minNotes}")
