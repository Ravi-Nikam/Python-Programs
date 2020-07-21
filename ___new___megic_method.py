class Example:
    def __new__(self):
        return 1,"r"

    
# creating object of the class Example
mutantObj = Example()

# but this will return that our object 
# is of type str
print(type(mutantObj))
