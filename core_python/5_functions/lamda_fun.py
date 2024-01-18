# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments: expression
multiply = lambda a,b : a*b 

print(multiply(2,3))
#so use lambda function when required for short period of time

#map,filter,reduce
arr=[1,2,3,4]
def myfun(x):
    return x*2

result=map(myfun,arr) #or
result = map(lambda a : a*2 , arr)
print(list(result))

def even_finder(x):
    if x%2==0:
        return x
 
#result2= filter(even_finder,arr)  or
result2= filter(lambda a:a%2==0, arr)
print(list(result2))

from functools import reduce  

result3 = reduce(lambda a,b: a if a>b else b,arr)
print(result3)
