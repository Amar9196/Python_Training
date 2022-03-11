import os

myfilew = open("mypython.txt", "w")
myfilew.write("This is a test myfile\n")
myfilew.write("This is to test myfile handling in python\n")
myfilew.write("This is a end line\n")
myfilew.close();
print("My file is created.\n")

myfile = open("mypython.txt", "r")
lines = myfile.readlines()
for line in lines:
    print(line)
myfile.close()

print("----------------")


myfile = open("mypython.txt", "r")
print(myfile.tell())
myfile.readline()
print(myfile.tell())
myfile.close();

print("----------------")
myfile = open("mypython.txt", "r+")
print(myfile.tell())
myfile.seek(21)
myfile.write("HTC")
print(myfile.tell())
myfile.close();
print("My file size is:" , os.path.getsize("mypython.txt"))