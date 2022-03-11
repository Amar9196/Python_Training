'''
Created on 29-May-2019

@author: srilakshmig
'''
#import abc
from abc import ABCMeta,abstractmethod


class ShopInterface(metaclass=ABCMeta):

    @abstractmethod 
    def create_pet(self, p1):
        pass
    @abstractmethod 
    def read_pet(self,pId):
        pass
    @abstractmethod 
    def read_all_pet(self):
        pass
    @abstractmethod 
    def update_age(self, pId, age):
        pass
    @abstractmethod 
    def update_price(self,pId,price):
        pass
    @abstractmethod 
    def delete_pet(self,pId):
        pass
    
    