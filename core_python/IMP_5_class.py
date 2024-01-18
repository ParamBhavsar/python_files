# class is a blueprint for an object / object is an instance of the class

#class myclass:
#All classes have a function called __init__(), 
# which is always executed when the class is being initiated.    
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created

# Note: The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.

#Note: The __init__() function is called automatically every time the class is being used to create a new object.

class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    

u1 =  user("param",19)
print(u1)  #<__main__.user object at 0x000001AD3A079B50>
#Because you its printing an object, and that object doesn't have a __repr__ or __str__ method explaining how to print it.
#The __str__() function controls what should be returned when the class object is represented as a string.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self): 
        return f"your name is {self.name}"

p1=person("param",19)
print(p1)

# Objects can also contain methods. 
# Methods in objects are functions that belong to the object.

class person2:
    def __init__(self,name):
        self.name=name
    
    def myfunc(self):
        print("hello "+ self.name)

p=person2("param")
p.myfunc()
p.name="new_param" # modify properties
p.myfunc()

        