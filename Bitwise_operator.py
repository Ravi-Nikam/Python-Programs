#Bitwise operators: Bitwise operators acts on bits and performs bit by bit operation.

def oper(x):
    print(bin(x))


x=int(input("Enter the no1:"))
y=int(input("Enter the no2:"))
oper(x)
oper(y)


#Print bitwise AND operation
ans=x&y
print("bitwise AND=>",bin(ans))

#Print bitwise OR operation
ans=x|y
print("bitwise OR=>",bin(ans))

#Print bitwise NOT operation
ans=~x
ans1=~y
print("bitwise NOT =>",bin(ans),bin(ans))

# print bitwise XOR operation 
ans=x^y
print("bitwise XOR=>",bin(ans))

# print bitwise right shift operation
ans=x>>y
print("bitwise Right_Shift=>",bin(ans))

# print bitwise Left shift operation
ans=x<<y
print("bitwise Left_Shift=>",bin(ans))






    
