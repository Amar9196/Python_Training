'''
Created on Jul 19, 2019

@author: srilakshmig
'''

import configparser
import psycopg2


class dbconnection:

    def __init__(self):
        pass

    @staticmethod    
    def get_connectionobj():
        config = configparser.RawConfigParser()
        config.read('configfile.properties')
        
        dbname= config.get('dbconnect','dbname')
        username= config.get('dbconnect','username')
        server= config.get('dbconnect','server')
        password= config.get('dbconnect','password')
        
        conn = psycopg2.connect("dbname='" + dbname + "' user='" + username + "'host='" + server + "'password='" + password + "'")   
        return conn   

