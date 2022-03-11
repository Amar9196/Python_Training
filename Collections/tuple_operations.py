'''
Created on Jul 16, 2019

@author: srilakshmig
'''


my_data = ("hi", "hello", "bye")
print(my_data)

# tuple of int, float, string
my_data2 = (1, 2.8, "Hello World")
print(my_data2)

# tuple of string and list
my_data3 = ("Book", [1, 2, 3])
print(my_data3)

# tuples inside another tuple
# nested tuple
my_data4 = ((2, 3, 4), (1, 2, "hi"))
print(my_data4)

#Declaring a single tuple element
# my_data = (99,)

#Accessing tuple Element
print(my_data[2])
print(my_data[-3])#reverse indexing
print(my_data4[1][1])

#Deleting a Tuple
del my_data

#iterating a Tuple
for my in my_data2:
     print(my)