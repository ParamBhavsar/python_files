# The split() method splits a string into a list/array.
# You can specify the separator, default separator is any whitespace.
txt2= "hello i am the king of new york"
print(txt2.split())  #default split in whitespace

txt3 = "param#king#newyork#soon&yes"
print(txt3.split("#"))  # will split throughout when # occurs
# can specify how many max split
print(txt3.split("#",1)) # will create array of size 1 with spllitting #