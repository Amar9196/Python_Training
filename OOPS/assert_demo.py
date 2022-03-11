'''
Created on Jul 17, 2019

@author: srilakshmig
'''
try:
    num=int(input("Enter a even number:"))
    assert num%2==0,"You have entered a invalid input or odd number"
except AssertionError as obj:
    print(obj)

print("After the assertion")
