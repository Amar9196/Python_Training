'''
Created on Jul 16, 2019

@author: srilakshmig
'''
a=[2,4,6,8]
b=[1,2,3,4]
result=[] # List li = new ArrayList();

for i in a:
    if i in b:
        result.append(i)
        
result=[i for i in a if i in b]        
        
print(result)

lst=[]
for x in range(1,11):
    lst.append(x**3)
print(lst)

'''
#For printing the cube of numbers
lst=[]
lst=[x**3 for x in range(1,11)]
print(lst)
'''
    