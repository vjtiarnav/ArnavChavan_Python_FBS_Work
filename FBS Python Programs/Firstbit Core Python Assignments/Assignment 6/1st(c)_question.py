'''
Output:
      1   
    1   1   
  1   2   1   
1   3   3   1
'''
for i in range(1,5):
    
    num = 1
    
    for j in range(1,5-i):
        print(" ", end = " ")
        
    for j in range(0,i):
        print(num, end="   ")
        num = num * (i - 1 - j) // (j + 1)
        
    print()