# A set is a collection of data which is *unordered, *unchangeable*, and unindexed*.
# written within a curly braces{ }
#Once a set is created, you cannot change its items, 
#but you can remove items and add new items.
# ** not allow duplicates as not indexed 

myset={"hi","hello",1,True}
print(type(myset)) #<class 'set'>
myset.add("new"); print(myset)
myset.remove("hi"); print(myset)

#Both union() and update() will exclude any duplicate items.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
thisset.union(myset)
print(thisset) #random order 

# to remove sets use myset.remove("") but it throws error if no element is in the set
# can use myset.dicard("") will not throw an error if no elements in the set
# can use .pop() but it is random as set are unindexed 
thisset.remove("apple")
print(thisset)
