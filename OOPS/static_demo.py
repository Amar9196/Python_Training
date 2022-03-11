'''
Created on Jul 17, 2019

@author: srilakshmig
'''
class ObjectCounter:
    
    numberOfObjects = 0
    
    def __init__(self):
        ObjectCounter.numberOfObjects+=1
    
    @staticmethod    
    def displayCount():
        print(ObjectCounter.numberOfObjects)
        
o1= ObjectCounter()
o2=ObjectCounter()

ObjectCounter.displayCount()