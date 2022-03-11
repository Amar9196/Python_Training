'''
Created on Jul 16, 2019

@author: srilakshmig
'''

myDict = {}
myDict["workPhone"] = "04423332435"
myDict["persPhone"] = 9877767776
myDict[1] = "sa3432"
myDict["workPhone"] = "04423332435"

print(myDict["workPhone"])
print("adhar-Id:",myDict[1])

myDict = {"id":5432,"name":"samyukta","designation":"Gen Manager"}
print("Id:",myDict["id"])
print(myDict)
print(myDict.keys())
print(len(myDict.keys()))
print(myDict.values())
print(type(myDict))

myDict = {"id":6654,"name":"SathiBabu","address":"Vizag"}
myDict["income"]=950000.0
print(myDict)
del myDict["address"]
print(myDict)


myDict2 = {"id":7654,"name":"Damodaran","address":"Chennai","salary":1200000.5}


myDict.update(myDict2)
print(myDict)
#if(myDict>myDict2):
#      print("myDict is higher")
#else:
#      print("myDict2 is higher")
