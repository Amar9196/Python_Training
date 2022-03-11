'''
Created on Jul 19, 2019

@author: srilakshmig
'''

import psycopg2

from xlrd import open_workbook


class dbconnection:
    connection = open_workbook("xl_connection.xls")
   
    def __init__(self):
        pass

    @staticmethod    
    def get_connectionobj():
        with open("connection.xls"):
            connection = open_workbook("connection.xls")
            sheet1= connection.sheet_by_name("Sheet1")
        dbname = sheet1.cell(0,1).value
        server = sheet1.cell(1,1).value
        username = sheet1.cell(2,1).value
        password = sheet1.cell(3,1).value 
        conn = psycopg2.connect("dbname='" + dbname + "' user='" + username + "'host='" + server + "'password='" + password + "'")   
        return conn   

