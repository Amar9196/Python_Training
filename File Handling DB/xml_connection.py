'''
Created on Jul 19, 2019

@author: srilakshmig
'''
import xml.etree.ElementTree as XmlReader
import psycopg2

class dbconnection:
    def __init__(self):
        pass

    @staticmethod    
    def get_connectionobj():

        XML_DOM=XmlReader.parse("xml_conn.xml")
        rootNode=XML_DOM.getroot()
        for item in rootNode:
            if(item.tag.__eq__('dbname')):
                dbname =item.text 
            if(item.tag.__eq__('server')):
                server = item.text
            if(item.tag.__eq__('username')):
                username = item.text
            if(item.tag.__eq__('password')):
                password = item.text  
        conn = psycopg2.connect("dbname='" + dbname + "' user='" + username + "'host='" + server + "'password='" + password + "'")   
        return conn   

print(dbconnection.get_connectionobj())       
        