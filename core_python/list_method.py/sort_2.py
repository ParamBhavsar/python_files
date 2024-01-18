arr_obj=[
    {"name":"param" ,"age":19},
    {"name":"ram" ,"age":59},
    {"name":"king" ,"age":14},
    {"name":"smith" ,"age":13},
]
# here we want to sort array of obj within age in desc order
def myfunc(e):
    return e["age"]

# this function returns year/age to sort and sort according to it 
arr_obj.sort(reverse=True,key=myfunc)
print(arr_obj)

arr2=[35,68,965,234]
arr2.reverse() 
print(arr2) # reverse the list not sort in descending order
