a=["bet","apple","deal","call"]
a2="5 4 3 2 1"
arr=a2.split(" ")
print(arr)

a.sort()
arr.sort()
print(a +  arr) #can concate 2 arrays **

#list.sort(reverse=True/False, key=myFunc)
# reverse=True will sort the list descending. Default is reverse=False
# key passes a function to specify the sorting criteria(s)

a3=["a","abc","ab","abdfdsf","assad"]
a4=a3.copy()

#now we want to sort it according to length of a2 so we pass a key

def myFunc(e):
    return len(e) # this will return length to key and sort it accordingly

a3.sort(key=myFunc) # note we here write without() 
print(a3)

#now we want to sort it in descending order of lenght 
a4.sort(reverse=True,key=myFunc)
print(a4) 
