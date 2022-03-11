try:
    pfile = open("product.txt", "w")
    pfile.write("PEN\n")
    pfile.write("PENCIL\n")
    pfile.write("ERASER\n")
except IOError as ex:
    print("Error-", ex)
finally:
    pfile.close()
    print("File created\n")

try:
    pfile = open("product.txt", "r")
    for line in pfile:
        print(line)
except IOError as ex:
    print(ex)
finally:
    pfile.close();

# with clause
with open("product.txt", "r") as pfile:
    for line in pfile:
        print(line)