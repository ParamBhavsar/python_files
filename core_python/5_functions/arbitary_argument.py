# if you don't know how many arguments will bw passsed to your function
# we use arbitary argument like def function (*arg): 
# this way a function will recive arguments in form of tuples(fixed and indexed) ,so 
# can access any element of the tuple inside the funciton 

def funciton(*arg):
    print("hello this is " + arg[1])

funciton("param","smith","sam")  

# default parameter is given to an parameter incase if no argument is passed to the fun

def funciton2(myname="param"):
    print("hello this is "+ myname)

funciton2()  

#function definitions cannot be empty,
#but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def function3(helloo):
    pass

#recursion 
def fibonaci(k):
    if(k==1 or k==2):
        return 1
    else:
        return fibonaci(k-1)+fibonaci(k-2)

print(fibonaci(10))