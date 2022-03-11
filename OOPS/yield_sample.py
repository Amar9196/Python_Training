'''
Created on Jul 16, 2019

@author: srilakshmig
'''
def nextSquare(): #2
    i = 1;  #3
    while True: #4   #11
        yield i*i   #5              
        i += 1     #10 
  
#program execution
for num in nextSquare(): #6 num =1 #9
    if num > 100: #7 
         break    
    print(num) #8