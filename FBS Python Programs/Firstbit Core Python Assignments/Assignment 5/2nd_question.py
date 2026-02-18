'''
Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students.
'''
num_students = int(input("Enter number of students: "))
total_percentage = 0

for i in range(num_students):
    print(f"Enter the marks obtained by student {i+1}: ")
    
    total_marks = 0
    for j in range(5):
        marks = int(input(f"Enter marks obtained in subject {j+1}: "))
        total_marks += marks
    
    percentage = (total_marks/500)*100
    
    total_percentage += percentage
    
    print(f"Percentage obtained by Student {i+1} is: {percentage:.2f}% ")
    print()

average_percentage = (total_percentage)/num_students
print(f"The average percentage scored by {num_students} is {average_percentage:.2f}%")
