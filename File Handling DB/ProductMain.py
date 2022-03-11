'''
Created on May 28, 2019

@author: srilakshmig
'''
from day5.Product import Product
from day5.ProductOperations import ProductOperations
# # import Entities

if __name__ == '__main__':

    pen=Product("S867","Pen","CT02",100,10.0)
    
    pencil=Product("S895","Pencil","CT03",1000,15.0)
     
       
    op=ProductOperations()
    op.add_prod_proc(pen)
    #op.add_prod(pen)
    op.add_prod(pencil)
    print("products are inserted")
     
    updatedProduct=op.read_prod("PR80")
    updatedProduct.set_prod_name("newPencil")
    op.update_prod(updatedProduct)
    print("product is updated")
      
      
    op.remove_prod("R895")
    print("Product is removed")
      
    for product in op.readall_prod():
        print(product)