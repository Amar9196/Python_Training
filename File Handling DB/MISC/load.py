import psycopg2
import xlrd
import json

book = xlrd.open_workbook("studentdetails.xlsx")
sheet = book.sheet_by_name("Sheet1")

jsonFile = open("connection.json",)
jsonReader=json.load(jsonFile)
dbname= jsonReader["dbname"]
user= jsonReader["user"]
host=jsonReader["host"]
password=jsonReader["password"]
conn = psycopg2.connect("dbname='"+dbname+"' user='"+user+ "'host='"+host+"'password='"+password+"'")

cursor = conn.cursor()

query = """INSERT INTO student (sid,name,age) VALUES (%s, %s, %s)"""

for r in range(1, sheet.nrows):
    sid = sheet.cell(r,0).value
    name = sheet.cell(r,1).value
    age = sheet.cell(r,2).value
    values = (sid,name,age)
    cursor.execute(query, values)

cursor.close()

conn.commit()

conn.close()

print("")
print("Load Operation Done..!!")
print("")



columns = str(sheet.ncols)
rows = str(sheet.nrows)
