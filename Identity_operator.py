"""Identity operators-
is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal does not imply that they are identical."""

a1 = 3
b1 = 3
a2 = 'GeeksforGeeks'
b2 = 'GeeksforGeeks'
a3 = [1,2,3] 
b3 = [1,2,3] 
  
  
print(a1 is not b1) 
  
  
print(a2 is b2) 
  
# Output is False, since lists are mutable. 
print(a3 is b3)
