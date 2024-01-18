a=["apple","banana",1,3]
b=[True,"adsa"]
c=a.copy()
print(c) #['apple', 'banana', 1, 3]

#list.insert(positon, elmnt)
a.insert(2,b)
print(a)     #['apple', 'banana', [True, 'adsa'], 1, 3]

print(a.count("apple"))    #1
