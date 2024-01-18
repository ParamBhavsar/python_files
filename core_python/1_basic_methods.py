
# note string methods returns desired changes to the new string and do not affect the
# original one to which the method was applied 
name = "PaRaM"

print(name.islower())  #check if is in lower case true or false
print(name.lower())  #returns new string of name with lowercase
# lly with isupper() and upper

print(name.isalpha()) # check if alphabet in name
print(f"{name.isdecimal()} {name.isspace()} {name.isalnum()} ")

#The endswith() method returns True if the string ends with the specified value, 
# otherwise False.
# string.endswith(value, start, end)
txt= "hello welcome to my world."
xx= txt.endswith("world.")
print(xx)