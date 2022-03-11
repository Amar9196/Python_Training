'''
Created on Jul 16, 2019

@author: srilakshmig
'''
# lst=[2,3,4,5]
from nntplib import lines

# result = list(map(lambda n:n*2,lst))
# print(result)
# print(lst)
input_list = ['San Jose', 'San Francisco', 'Santa se', 'Houston']
desireList = list(map(lambda x: x if x[0] == 'S' else '', input_list))
print(desireList)
desireList.remove('')
print(len(desireList))
# 
# "This is sample1 This is sample2" => "This,2" "is,2" "sample1, 1" "sample2,1"
# 1. split into lines 
# 2. lines -> words
# 3. words -> (word,1) (This,1)(is,1)(sample1,1)
# 4. sort (word,1) (is,1)(is,1) (sample,1)(sample2,1)(This,1)(This,1)
# 5. sum values of every word (is,2)(sample1,1)(sample2,1)(This,2)


