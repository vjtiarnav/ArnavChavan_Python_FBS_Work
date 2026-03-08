'''
Output:   A 
        A B C 
      A B C D E 
    A B C D E F G 
  A B C D E F G H I 
'''

for i in range(1,6):
    for j in range(1,7-i):
        print(" ", end = " ")
        
    ch = 65
    for j in range(1,2*i):
        print(chr(ch), end = " ")
        ch += 1
    print()