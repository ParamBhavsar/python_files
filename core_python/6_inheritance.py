# inheritance is oop concept in which child class can inherit the properties 
# of the parent class , by syntax class child (parent)

#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
#so, Python has a super() function 
#that will make the child class inherit all the methods and properties from its parent:

class parent:
    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name=l_name
    
class student(parent):
    def __init__(self, f_name, l_name,your_name):
        super().__init__(f_name, l_name) #to inherit all prop. of parent class else it will override the fun
        self.your_name=your_name
    
    def print_func(self):
        print(f"{self.your_name} {self.f_name} {self.l_name}")

student_object = student("sanjay","bhavsar","param") 
student_object.print_func()
# so we can access the methods of parent class using inheritance and then by creating object of student 
