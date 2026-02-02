# Write a program to calculate the percentage marks of a student based on marks of any 5 subjects

phy = int(input("Enter Physics marks: "))
chem = int(input("Enter Chemistry marks: "))
maths = int(input("Enter Maths marks: "))
cs = int(input("Enter Computer Science marks: "))
eng = int(input("Enter English marks: "))

totalMarks = (phy+chem+maths+cs+eng)

percentageMarks = (totalMarks/200)*100

print(f"The student scored {percentageMarks}%")