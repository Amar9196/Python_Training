'''
Created on Jun 12, 2019

@author: srilakshmig
'''

a,b,c=[int(x) for x in input("Enter three integer numbers").split()]
average = (a+b+c)/3
print("Average of the three numbers is:",average)


#for loop_var in range:
'''   

start=int(input("Enter the number"))#5
end=int(input("Enter the number"))#8
if (end>start):
    for num in range(start,end+1):
        count=0
        for i in range(2,int(num/2)):
            if(num%i==0):
                count=count+1
                break
        if((count==1) | (num==1)|(num==0)):
            pass
        else:
            print(num, " is a Prime number")
else:
    print("Incorrect Range")'''