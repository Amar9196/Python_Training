'''
Created on Jun 12, 2019

@author: srilakshmig
'''
salary = float(input("Enter salary:"))
house_emi = float(input("Enter housing emi:"))
edu_emi = float(input("Enter education emi:"))

salary = salary*12
houseEmi = house_emi*12
eduEmi = edu_emi*12

print("Your annual salary is ",salary)

gross_salary = salary-houseEmi-eduEmi
print("Your taxable salary is ",gross_salary)

if(gross_salary>1000000):
    tax = gross_salary-(gross_salary*0.3)
elif(gross_salary>500000):
    tax = gross_salary-(gross_salary*0.2)
else:
    tax = (gross_salary*0.05)
    
print("Your tax for the year is ",tax)