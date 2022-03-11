'''
Created on Jun 12, 2019

@author: srilakshmig
'''
date=int(input("Enter the date"))
month=int(input("Enter the month"))
year=int(input("Enter the year"))
if((month<=12) & (month>0)):
    if((month==1) | (month==3)| (month==5)| (month==7)| (month==8)| (month==10)| (month==12)):
        if((date>0) &(date<=31)):
            print("Valid date")
        else:
            print("Not a valid date")
    elif((month==4)| (month==6)|(month==9)|(month==11)):
        if((date>0)&(date<=30)):
            print("Valid date")
        else:
            print("Not a valid date")
    elif(month==2):
        if((year%4==0)&(year%100!=0)|(year%400==0)):
            if(date<=29):
                print("Valid date")
            else:
                print("Not a valid date")
        elif(date<=28):
                print("Valid date")
        else:
            print("Not a valid date")
else:
    print("Not a valid month")