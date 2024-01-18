name = "param"
age = 19
cgpa = 9.410

print(isinstance(name,str))   # wil check if name is isnstance of string gives true if it is else will give false
# similar way 
print(type(name)) # will returns type of datatype name is 
print(type(name)==str)  # will give true is == satisfies

print(isinstance(age,float))
print(isinstance(cgpa,float))

# bool
here=True
if here:
    print(f"done {here}")
else:
    print(here) 

#complex num
complex_num= 3+2j
#or
complex_num2=complex(3,2)  #both are true for complex declaration