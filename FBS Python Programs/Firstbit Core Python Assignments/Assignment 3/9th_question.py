# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

maths = int(input("Enter marks scored in Mathematics: "))
phy = int(input("Enter marks scored in Physics: "))
chem = int(input("Enter marks scored in Chemistry: "))
cs = int(input("Enter marks scored in Computer Science: "))
english = int(input("Enter marks scored in English: "))

totalMarks = maths + phy + chem + cs + english

if(totalMarks >= 85 or totalMarks <= 100):
    print("Your grade is A+")
elif(totalMarks >= 70 or totalMarks < 85):
     print("Your grade is A")
elif(totalMarks >= 55 or totalMarks < 70):
     print("Your grade is B")
elif(totalMarks >= 40 or totalMarks < 55):
     print("Your grade is C")
elif(totalMarks >= 35 or totalMarks < 40):
     print("Your grade is D")
else:
    print("Failed!!")