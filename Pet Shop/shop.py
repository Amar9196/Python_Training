'''
Created on 23-May-2019

@author: srilakshmig
'''
#from day3.pet import Pet
from day3.abstract import ShopInterface 
#from abc import  abstractmethod
    
class Shop (ShopInterface):
    def __init__(self,shop_id,shop_name,location,petlist=[]):
        self.__shop_id= shop_id
        self.__shop_name=shop_name
        self.__location=location
        self.__petlist=petlist 

    def get_shop_id(self):
        return self.__shop_id


    def get_shop_name(self):
        return self.__shop_name


    def get_location(self):
        return self.__location


    def get_petlist(self):
        return self.__petlist


    def set_shop_id(self, value):
        self.__shop_id = value


    def set_shop_name(self, value):
        self.__shop_name = value


    def set_location(self, value):
        self.__location = value


    def set_petlist(self, value):
        self.__petlist = value


    def del_shop_id(self):
        del self.__shop_id


    def del_shop_name(self):
        del self.__shop_name


    def del_location(self):
        del self.__location


    def del_petlist(self):
        del self.__petlist
    
    def create_pet(self, p1):
        self.__petlist.append(p1)
        
    def read_pet(self,pid):
        
        for pet in self.__petlist:
            if((pet.pet_id).__eq__(pid)):
                return pet
        return None
    def read_all_pet(self):
        return self.__petlist
    
    def update_age(self, pid,age):
        for pet in self.__petlist:
            if((pet.pet_id).__eq__(pid)):
                pet.set_age(age)
                return pet
        return None
    def update_price(self, pid,price):
        for pet in self.__petlist:
            if((pet.pet_id).__eq__(pid)):
                pet.set_price(price)
                return pet
        return None
    
    def delete_pet(self,pet_id):
        for pet in self.__petlist:
            if (pet.pet_id.__eq__(pet_id)):
                self.__petlist.remove(pet)
                return 1
        return None                
    
    
    shop_id = property(get_shop_id, set_shop_id, del_shop_id, "shop_id's docstring")
    shop_name = property(get_shop_name, set_shop_name, del_shop_name, "shop_name's docstring")
    location = property(get_location, set_location, del_location, "location's docstring")
    petlist = property(get_petlist, set_petlist, del_petlist, "petlist's docstring")
        
    def __repr__ (self):
        return (" Shop id "+ str(self.__shop_id)+ " Shop name "+ str(self.__shop_name)+ " Location "+str(self.__location)+ " Pet list "+str(self.__petlist))