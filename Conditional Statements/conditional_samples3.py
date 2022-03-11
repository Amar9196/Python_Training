'''
Created on Jul 12, 2019

@author: srilakshmig
'''

def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")

print(SwitchExample(2))
