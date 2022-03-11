'''
Created on 29-May-2019

@author: srilakshmig
'''
class InvalidPriceException(Exception):
    def __init__(self,value="Invalid Price Exception occured"):
        self.value=value
    def __str__(self):
        return repr(self.value)