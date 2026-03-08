'''
Output: 1 
        1 2 
        1   3 
        1     4 
        1 2 3 4 5 
'''
for i in range(1,6):
    for j in range(1,i+1):

        if(j == 1):
            print(1, end = " ")

        elif(j==i):
            print(i, end = " ")

        elif(i == 5):
            print(j, end = " ")

        else:
            print(" ", end = " ")
            
    print()