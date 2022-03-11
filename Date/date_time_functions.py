'''
Created on Jul 15, 2019

@author: srilakshmig
'''
import datetime
import time
import calendar

localtime = time.localtime(time.time())
print(localtime)

time_string = "21 June, 2018"
result = time.strptime(time_string, "%d %B, %Y")
print(result)

named_tuple = time.localtime() # get struct_time
print(named_tuple.tm_year)
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print(time_string)


calendar.setfirstweekday(6)
cal = calendar.month(2019, 2)
print(cal)

cal=calendar.monthrange(2019, 7)
print(cal)

print(calendar.isleap(2020))

cal=calendar.calendar(2019,w=2,l=1,c=6)
print(cal)



