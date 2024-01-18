#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

users={"name":"param","age":19,"address":"gandhinagar"}
print(users)
print(users["name"]) # to acces certain key value of user dictionaries

# Dictionaries cannot have two items with the same key:

#to change the values
users["address"]="GEB"
print(users)
#or
users.update({"age":18})
print(users)
#also add new value
users.update({"clg":"ldrp"})
print(users)
#to remove the key value
users.pop("age") ;print(users)

#nested dictionaries
family={
    "child1":{"name":"xyz","age":12},
    "child2":{"name":"abc","age":13}
}
#to access age of child2 
print(family["child2"]["age"])
