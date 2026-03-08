'''
Output: *   *   *   *   *  
        *               *  
        *               *  
        *               *  
        *               *  
        *   *   *   *   *  
'''

rows = int(input("Enter number of rows: ")) # Input 6
columns = int(input("Enter number of columns: ")) # Input 5

for i in range(1,rows+1):
    for j in range(1,columns+1):
        if(i == 1 or i == rows or j == 1 or j == columns):
            print(" * ", end = " ")
        else:
            print("   ", end = " ")
    print()