'''
Output: 1 2 3 4 5 
        2     5 
        3   5 
        4 5 
        5 
'''
for i in range(1,6):
    
    for j in range(1,7-i):
        
        if (i ==1 or j == 5):
            print(j, end = " ")
            
        elif(i==5 or j == 1):
            print(i, end = " ")
            
        elif(j == 6-i):
            print(5, end = " ")
            
        else:
            print(" ", end = " ")
            
    print()
