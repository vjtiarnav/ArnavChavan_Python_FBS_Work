'''
Output:
         *  
       *   *  
     *       *  
   *           *  
 *               *  
 *               *  
   *           *  
     *       *  
       *   *  
         *  
'''

# Logic 1

for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end = " ")
    
    for j in range(1,i+1):
        if(j == 1 or j == i):
            print(" * ", end = " ")
        else:
            print("   ", end = " ")
    print()
    
for i in range(1,6):
    for j in range(1,i+1):
        if(i==1 or j == i):
            print(" * ", end = " ")
        else:
            print(" ", end = " ")
            
    for j in range(1,6-i):
        if(j == 5-i):
            print(" * ", end = " ")
        else:
            print("   ", end = " ")
      
    print()


# Logic 2

for i in range(1,6):                             
    for j in range(1,10):
        if(j == 6-i or j == i+4):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
    
for i in range(1,6):
    for j in range(1,10):
        if(j == i or j == 10-i):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
            
'''
Output:         
        *         
      *   *       
    *       *     
  *           *   
*               * 
*               * 
  *           *   
    *       *     
      *   *       
        *  
'''