'''
Created on May 28, 2019

@author: srilakshmig
'''

import json
import psycopg2

#  Reading data from json object inside json file    


class dbconnection:

    def __init__(self):
        pass

    @staticmethod    
    def get_connectionobj():
        with open("config.json") as jsonFile:
            jsonReader = json.load(jsonFile)
        dbname = jsonReader["dbconfig"]["dbname"]
        server = jsonReader["dbconfig"]["server"]
        username = jsonReader["dbconfig"]["username"]
        password = jsonReader["dbconfig"]["password"]  
        conn = psycopg2.connect("dbname='" + dbname + "' user='" + username + "'host='" + server + "'password='" + password + "'")   
        return conn   



