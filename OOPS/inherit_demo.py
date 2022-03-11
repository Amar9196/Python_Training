'''
Created on Jul 17, 2019

@author: srilakshmig
'''
class Employee:
    def __init__(self,id,name):
        self.__id = id
        self.__name=name
    def displayEmp(self):
        print("The id is {0} and the name is {1}".format(self.__id, self.__name))

class FullTimeEmployee(Employee):
    def __init__(self,shift,id,name):
        super().__init__(id, name)
        self.__shift = shift
    def displayEmp(self):
        super().displayEmp()
        print("The shift is ",self.__shift)

femp = FullTimeEmployee("Gen",101,"sri")
femp.displayEmp()