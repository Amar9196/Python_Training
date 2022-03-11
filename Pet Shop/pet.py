'''
Created on 23-May-2019

@author: srilakshmig
'''
# constructor, private members, getters and setter, str, repr, hash,__eq__


class Pet:
    pet_distributor = "ABC distributor"#class variable
    def __init__(self,pet_id,pet_name,pet_type,breed,gender,age,price):
        self.__pet_id= pet_id   #instance variables
        self.__pet_name=pet_name
        self.__pet_type=pet_type
        self.__breed=breed
        self.__gender=gender
        self.__age=age
        self.__price=price

    def get_pet_id(self):
        return self.__pet_id


    def get_pet_name(self):
        return self.__pet_name


    def get_pet_type(self):
        return self.__pet_type


    def get_breed(self):
        return self.__breed


    def get_gender(self):
        return self.__gender


    def get_age(self):
        return self.__age


    def get_price(self):
        return self.__price


    def set_pet_id(self, value):
        self.__pet_id = value


    def set_pet_name(self, value):
        self.__pet_name = value


    def set_pet_type(self, value):
        self.__pet_type = value


    def set_breed(self, value):
        self.__breed = value


    def set_gender(self, value):
        self.__gender = value


    def set_age(self, value):
        self.__age = value


    def set_price(self, value):
        self.__price = value


    def del_pet_id(self):
        del self.__pet_id


    def del_pet_name(self):
        del self.__pet_name


    def del_pet_type(self):
        del self.__pet_type


    def del_breed(self):
        del self.__breed


    def del_gender(self):
        del self.__gender


    def del_age(self):
        del self.__age


    def del_price(self):
        del self.__price

    pet_id = property(get_pet_id, set_pet_id, del_pet_id, "pet_id's docstring")
    pet_name = property(get_pet_name, set_pet_name, del_pet_name, "pet_name's docstring")
    pet_type = property(get_pet_type, set_pet_type, del_pet_type, "pet_type's docstring")
    breed = property(get_breed, set_breed, del_breed, "breed's docstring")
    gender = property(get_gender, set_gender, del_gender, "gender's docstring")
    age = property(get_age, set_age, del_age, "age's docstring")
    price = property(get_price, set_price, del_price, "price's docstring")


    def __repr__(self):
        return (" Pet id  "+str(self.__pet_id)+" Pet Name "+str(self.__pet_name)+ " Type "+str(self.__pet_type)+" Breed "+str(self.__breed)+" Gender "+str(self.__gender)+" Age "+str(self.__age)+" Price "+str(self.__price))
#     def str(self):
#             return (" Pet id  "+str(self.__pet_id)+" Pet Name "+str(self.__pet_name)+ " Type "+str(self.__pet_type)+" Breed "+str(self.__breed)+" Gender "+str(self.__gender)+" Age "+str(self.__age)+" Price "+str(self.__price))
#     
    def __eq__(self, other):
        return self.age == other.age and self.__breed == other.__breed

    def __hash__(self):
        print('The hash is:')
        return hash((self.__age))

