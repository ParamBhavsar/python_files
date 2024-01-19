# the string.format() method allows you to format the string according to requirements
# to format some part of string add it in {} braces wwhich you further wanna format
# Sometimes there are parts of a text that you do not control, 
#maybe they come from a database, or user input? **

txt="hello my name is {} and {} years old."
name = "param" ; age = 18
print(txt.format(name,age))

# if you want to refer to the same value more than once, use the index number:
txt ="hello {0} ,how are {1},hope {1} are {2}"
you ="you" ; cond="fine"
print(txt.format(name,you,cond)) # so you indx is 1 so will be placed where {1} in string

#can also use named inded
txt ="hello {user} ,how are {you},hope {you} are {fine}"
print(txt.format(user="param",you="you",fine="fine"))