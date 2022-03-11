'''
Created on Jul 16, 2019

@author: srilakshmig
'''
#string, tuple, list, set, dict

my_set = set("HelloWorld")
# print(my_set)

# iter_set = my_set.__iter__()
# for i in iter_set:
#     print(i)
# # 
# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# s1 = set()
# print(type(s1))
# # add list and set
# # Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)
# 
# 
# # pop an element
# # Output: random element
print(my_set.pop())
# 
# # pop another element
# # Output: random element
my_set.pop()
# print(my_set)
# 
# # clear my_set
# #Output: set()
my_set.clear()
print(my_set)
# 
# ######Set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
 
# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
A.union(B)
# 
print(A & B)
#A.intersection(B)
print(A - B)
# #A.difference(B)
print(A ^ B)
# #A.symmetric_difference(B)
 