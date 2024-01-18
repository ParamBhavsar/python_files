#Tuples are used to store multiple items in a single variable.
#tuples are *ordered and unchangable* written within round brackets 
mytuple=("hi","hello",1,True)   #can contain duplicate elements as indexed 
# A tuple can contain different data types:
print(type(mytuple))  #<class 'tuple'>
print(mytuple[-1])
print(mytuple[2])

#though Tuples are unchangeable ,
#to update tuples , You can convert the tuple into a list, change the list, 
#and convert the list back into a tuple.  
mytuple2= ("hi","hello",1,True) 
y = list(mytuple2)
y[1] = "new_hello"
mytuple2 = tuple(y)
print(mytuple2)


# lly we can add items too by same method using append
mytuple3= ("hi","hello",1,True) 
y2 =list(mytuple3); y2.append("new")
mytuple3=tuple(y2)
print(mytuple3)

# we can join and multiply tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 
print(tuple1*2) #('a', 'b', 'c', 'a', 'b', 'c')