'''
Created on May 28, 2019

@author: srilakshmig
'''


from day5.Product import Product
from day5.dbconnection import dbconnection

class ProductOperations(object):
    def add_prod(self,prod_obj):
        #con = dbconnection.get_connectionobj()
        con=dbconnection.get_connectionobj();
        cur = con.cursor()
        cur.execute("INSERT INTO Product values (%s,%s,%s,%s,%s)",(prod_obj.get_prod_id(),prod_obj.get_prod_name(),prod_obj.get_cat(),prod_obj.get_qty_on_hand(),prod_obj.get_prod_price()))
        con.commit()
        cur.close()
        con.close()
    def remove_prod(self,prod_id):
        con = dbconnection.get_connectionobj()
        cur = con.cursor()  
        cur.execute("DELETE FROM Product WHERE product_code = '%s'"%(prod_id))
        con.commit()
        cur.close()
        con.close()
    def update_prod(self,prod_obj):
        con = dbconnection.get_connectionobj()
        cur = con.cursor()  
        cur.execute("UPDATE Product SET prod_desc=%s,category_code=%s,price=%s,qty_on_hand=%s WHERE product_code=%s",(prod_obj.get_prod_name(),prod_obj.get_cat(),prod_obj.get_prod_price(),prod_obj.get_qty_on_hand(),prod_obj.get_prod_id()))        
       
        con.commit()
        cur.close()
        con.close()
    def read_prod(self,prod_id):
        con = dbconnection.get_connectionobj()
        cur = con.cursor()
        cur.execute("SElECT *  FROM Product WHERE product_code='%s'"%(prod_id))
        foundProduct = cur.fetchone()
        #con.commit()
        cur.close()
        con.close()
        
        return Product(foundProduct[0],foundProduct[1],foundProduct[2],foundProduct[3],foundProduct[4])
    def readall_prod(self):
        con = dbconnection.get_connectionobj()
        cur = con.cursor()
        cur.execute("SElECT *  FROM Product ")
        foundproducts = cur.fetchall()
        #con.commit()
        cur.close()
        con.close()
        return foundproducts 
    def add_prod_proc(self,prod_obj):
        #con = dbconnection.get_connectionobj()
        con=dbconnection.get_connectionobj();
        cur = con.cursor()
        cur.callproc('usp_insert_product',[prod_obj.get_prod_id(),prod_obj.get_prod_name(),prod_obj.get_cat(),prod_obj.get_prod_price(),prod_obj.get_qty_on_hand()])
        con.commit()
        cur.close()
        con.close()
