'''
Created on Jul 16, 2019

@author: srilakshmig
'''

import re
import day2.email_validation as v_email

str = "Take 1 op 1-3-2019 One 23 idea.One idea 45 at a Time 12-11-2020"
result = re.search(r'O\w+', str)
print(result.group())

result = re.findall(r'O\w+', str)
print(result)

result = re.match(r'T\w\w', str)
print(result.group())

result = re.sub(r'One', 'Two', str)
print(result)

result = re.findall(r'O\w\w', str)
print(result)

#"12 or 1"
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)

result = re.search(r'^T\w*', str)
print(result.group())

xx = "This is a sample re program"
r1 = re.findall(r"^\w+", xx)
print(r1)
print((re.split(r'\s',xx)))
print((re.split(r's',xx)))


if v_email.isValidEmail("abc12345@gmail.come")==True:
    print("This is a valid address")
else:
    print("This is not a valid email address")






