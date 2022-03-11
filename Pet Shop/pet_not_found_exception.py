'''
Created on 29-May-2019

@author: srilakshmig
'''
class PetNotFoundException(Exception):
    def __init__(self,value="PetNotFound exception occured"):
        self.value=value
    def __str__(self):
        return repr(self.value)