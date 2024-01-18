# A variable created inside a function belongs to the local scope of that function,
# and can only be used inside that function

x = 200         # global variable

def local_function():
    y=100       # local variable
    print(x)
    print (y)

local_function()

print(x)

#The global keyword makes the variable global.

a = 10

def local_function2():
    # global b = 22 Statements must be separated by newlines or semicolons
    global b 
    b = 22
    print(b)

print(a) #10 global 
local_function2()  # call the function to access b
print(b) # after calling the fn b can now be used in the global scope

