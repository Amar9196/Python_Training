'''
Created on Jul 17, 2019

@author: srilakshmig
'''
class Car:
    def __init__(self,make,year):
        self.make=make
        self.year=year
        
    class Engine:
        def __init__(self,number):
            self.number=number
        def start(self):
            print("Engine Started")
            
c = Car("BMW",2017)
e = c.Engine(123)
e.start()