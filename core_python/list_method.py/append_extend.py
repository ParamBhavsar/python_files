a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a) #['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo']]

#another way
a2=["apple", "banana", "cherry"]
b2=["Ford", "BMW", "Volvo"]
a2+=b2
print(a2)  #['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# Append function in Python adds a single element to the end of the list,
# whereas the extend function adds multiple elements (from an iterable) to the list

a3=["apple", "banana", "cherry"]
b3=["Ford", "BMW", "Volvo"]
a3.extend(b3)
print(a3)   #['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

b4="param"
a3.extend(b4)
print(a3) #['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo', 'p', 'a', 'r', 'a', 'm']