#reading connection properties from json file

import json
jsonFile = open("connection.json",)
jsonReader=json.load(jsonFile)
dbname= jsonReader["dbname"]
user= jsonReader["user"]
host=jsonReader["host"]
password=jsonReader["password"]

print(dbname,user,host,password)