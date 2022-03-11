'''
Created on 23-May-2019

@author: srilakshmig
'''
from day3.pet import Pet
from day3.shop import Shop
from day3.pet_not_found_exception import PetNotFoundException
from day3.invalid_price_exception import InvalidPriceException
if __name__== "__main__":
    
    p1=Pet(101,'Tommy','Dog','German Shepherd', 'Male', 1, 15000)
    p2=Pet(102,'Jamie','Cat','abc', 'Male', 2, 10000)
    p3=Pet(103,'Dany','Dog','Labrador', 'Female', 3, 8500)
    p4=Pet(104,'Jon','Dog','Dolmation', 'Male', 1, 15000)
    p5=Pet(105,'Rhaegal','Dog','Golden Retriever', 'Male', 1, 25000)
    p6=Pet(106,'Drogon','Cat','abc', 'Male', 1, 10000)
    p7=Pet(107,'Viserion','Cow','Jersey', 'Male', 1, 9500)
    p8=Pet(108,'Johnny','Cow','Jersey', 'Male', 1, 12500)
    p9=Pet(109,'Robert','Dog','Dolmation', 'Male', 1, 17000)
    p10=Pet(110,'Cersei','Cow','Jersey', 'Female', 2, 20000)
    p11=Pet(111,'Bran','Dog','Labrador', 'Male', 1, 15000)
    
    petlist=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]
    s1= Shop(201,"Abc pet shop", "Abc strret,xyz area", petlist)
    print(s1)
    while(True):
         print("1.Create 2.Read 3.Update 4.Delete 5.Exit")
         option=int(input("Enter your choice: "))
         
         if(option==1):
             p12=Pet(112,'gg','joi','klop','lpoit',4,8907)
             s1.create_pet(p12)
             print(s1)
         
         elif(option==2):
             print("1.Read 2.Read All")
             select=int(input("Enter your choice: "))
             if(select==1):
                 pet_id=int(input("Enter the id"))
                 read=s1.read_pet(pet_id)
                 if(read!=None):
                     print(read)
                 else:
                     try:
                         raise PetNotFoundException()
                     except PetNotFoundException as e:
                         print(e)
                     except Exception as e:
                         print(e)
                     finally:
                         print("Finally")
             if(select==2):
#                 read1= s1.read_all_pet()
#                 print(read1)
#         
#         elif(option==3):
#             print("List of options that can be updated: 1.Age 2.Price")
#             choice=int(input("Enter your choice :"))
#             if(choice==1):
#                 pet_id=int(input("Enter the id"))
#                 age=int(input("Enter age"))
#                 updated_pet = s1.update_age(pet_id, age)
#                 if(updated_pet)!=None:
#                     print(updated_pet)
#                 else:
#                     try:
#                         raise PetNotFoundException()
#                     except PetNotFoundException as e:
#                         print(e)
#             
#         
#             elif(choice==2):
#                 pet_id=int(input("Enter the id"))
#                 price=int(input("Enter price"))
#                 updated_pet = s1.update_price(pet_id, price)
#                 if(price>0):
#                     if(updated_pet)!=None:
#                         print(updated_pet)
#                     else:
#                         try:
#                             raise PetNotFoundException()
#                         except PetNotFoundException as e:
#                             print(e)
#                 else:
#                     try:
#                         raise InvalidPriceException()
#                     except InvalidPriceException as e:
#                         print(e)
#         
#         elif(option==4):           
#             pet_id=int(input("Enter the id"))
#             delete= s1.delete_pet(pet_id)
#             if(delete)!=None:
#                 print("The record is deleted")
#                 print(s1)
#             else:
#                 try:
#                         raise PetNotFoundException()
#                 except PetNotFoundException as e:
#                         print(e)
#         elif option == 5:
#             exit()    
#        
   
       
       
        
         
       
       