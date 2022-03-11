'''
Created on May 28, 2019

@author: srilakshmig 
'''


class Product():

    def __init__(self, prod_id, prod_name,cat, qty_on_hand, prod_price):
        self.__prod_id = prod_id
        self.__prod_name = prod_name
        self.__cat=cat
        self.__qty_on_hand = qty_on_hand
        self.__prod_price = prod_price

    def __str__(self):
        return object.__str__(self)



    def get_prod_id(self):
        return self.__prod_id


    def get_prod_name(self):
        return self.__prod_name


    def get_qty_on_hand(self):
        return self.__qty_on_hand

    def get_cat(self):
        return self.__cat
        
    def get_prod_price(self):
        return self.__prod_price


    def set_prod_id(self, value):
        self.__prod_id = value


    def set_prod_name(self, value):
        self.__prod_name = value

    def set_cat(self,value):
        self.__cat=value
    
    def set_qty_on_hand(self, value):
        self.__qty_on_hand = value


    def set_prod_price(self, value):
        self.__prod_price = value


    def del_prod_id(self):
        del self.__prod_id


    def del_prod_name(self):
        del self.__prod_name

    def del_cat(self):
        del self.__cat
    
    
    def del_qty_on_hand(self):
        del self.__qty_on_hand


    def del_prod_price(self):
        del self.__prod_price

    prod_id = property(get_prod_id, set_prod_id, del_prod_id, "prod_id's docstring")
    prod_name = property(get_prod_name, set_prod_name, del_prod_name, "prod_name's docstring")
    qty_on_hand = property(get_qty_on_hand, set_qty_on_hand, del_qty_on_hand, "qty_on_hand's docstring")
    prod_price = property(get_prod_price, set_prod_price, del_prod_price, "prod_price's docstring")
    cat = property(get_cat, set_cat, del_cat, "cat's docstring")

        
  
        
        
        
        
        
        
        
        
        
        
        
        
        