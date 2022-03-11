'''
Created on Jul 16, 2019

@author: srilakshmig
'''
theList = ['a','e','i','o','u']

def matchall(theList, value, pos=0):
    loc = pos - 1
    if value in theList:
        loc = theList.index(value, loc+1)
        yield loc
   

value = 'i'
for loc in matchall(theList, value):
    print("match at", loc+1, "position.")