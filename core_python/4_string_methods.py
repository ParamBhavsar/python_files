
# note string methods returns desired changes to the new string and do not affect the
# original one to which the method was applied 
name = "PaRaM"

print(name.islower())  #check if is in lower case true or false
print(name.lower())  #returns new string of name with lowercase
# lly with isupper() and upper

print(name.isalpha()) # check if alphabet in name
print(f"{name.isdecimal()} {name.isspace()} {name.isalnum()} ")

x=name.replace("RaM","xx") #replace("old","new",count/occurance)
print(x) 
user="one one one is two two"
print(user.replace("one","three",2)) # will only change first 2 one 

txt = "Hello, welcome to my world world."
#find() and #index are similar returns the first occurance index but find() returns -1
#and #index returns error
print(f"{txt.index("w")} ,{txt.find("w")} , {txt.find("q")} , {txt.rindex("world")}")
# rindex()	Searches the string for a specified value and returns the last position of
# where it was found print

#The endswith() method returns True if the string ends with the specified value, 
# otherwise False.
# string.endswith(value, start, end)

xx= txt.endswith("world.")
print(xx)

# The split() method splits a string into a list/array.
# You can specify the separator, default separator is any whitespace.
txt2= "hello i am the king of new york"
print(txt2.split())  #default split in whitespace

txt3 = "param#king#newyork#soon&yes"
print(txt3.split("#"))  # will split throughout when # occurs
# can specify how many max split
print(txt3.split("#",1)) # will create array of size 1 with spllitting #

