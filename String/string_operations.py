'''
Created on Jul 15, 2019

@author: srilakshmig
'''
s = "Welcome to python programming"
s1="""This is line 1
This is line 2
This is line 3"""

print(s1)

# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 23
print("The first occurrence of the letter a = %d" % s.index("a"))

#prints the index where it finds the string
print("find",s.find("to",0,20))

#replaces the second string with the first
print(s.replace("python", "pyspark"))

# Number of a's should be 1
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just index 12
print("The characters with odd index are '%s'" %s[0::3]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
print("Prints all except the last ", s[:-1] )
print("Prints the even index between 0 & 9",s[0:9:2])
print("Prints the reverse of the string from 15 ",s[15::-1])
print("Prints the reverse of the string",s[::-1])

#trim operation
print(s.strip())
print(s.lstrip())
print(s.rstrip())


# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.casefold())

# Check how a string starts
if s.startswith("Wel"):
    print("String starts with 'Wel'. Good!")

# Check how a string ends
if s.endswith("ing"):
    print("String ends with 'ing!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))