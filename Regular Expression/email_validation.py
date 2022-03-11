'''
Created on Jul 16, 2019

@author: srilakshmig
'''
import re
def isValidEmail(email):
    if len(email)>7:
        #srilakshmig@gmail.com 
        if re.match("^\w+@([a-z]|[A-Z])+\.([a-z A-Z]{2,3})$",email):
            return True
        return False
        

