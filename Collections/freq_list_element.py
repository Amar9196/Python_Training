'''
Created on Jul 16, 2019

@author: srilakshmig
'''
List = [2, 1, 2, 2, 1, 3, 1] 
def most_frequent(): 
    counter = 0
    num = set()
      
    for i in List: 
        curr_frequency = List.count(i) 
        #print(i,curr_frequency)
        if(curr_frequency >= counter): 
            counter = curr_frequency 
            num.add(i)
    return num
     
 
n=most_frequent()
print(n)
#print(List.count(1))
    