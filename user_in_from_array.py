from array import *

val=array('i',[]) #user defined array

length=int(input("Enter the length of array:"))

for i in range(length):
	x=int(input("Enter the value{}==>".format(i)))
	print("\n")
	val.append(x)


print(val)
