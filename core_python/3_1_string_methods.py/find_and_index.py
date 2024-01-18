txt = "Hello, welcome to my world world."
#find() and #index are similar returns the first occurance index but find() returns -1
#and #index returns error
print(f"{txt.index("w")} ,{txt.find("w")} , {txt.find("q")} , {txt.rindex("world")}")
# rindex()	Searches the string for a specified value and returns the last position of
# where it was found print