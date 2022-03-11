'''
Created on Jul 17, 2019

@author: srilakshmig
'''
from abc import abstractmethod,ABC

class Ab_Demo(ABC):
    @abstractmethod
    def disp(self):
        pass

class child(Ab_Demo):
    def display(self):
        print("From child")
    def disp(self):
        print("from disp")
ch = child()
ch.display()
ch.disp()
