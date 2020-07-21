a=5  #101
b=6	 #110

#temp=a
#a=b
#b=temp

#a=a+b   #11
#b=a-b	#5
#a=a-b   #6


print("value of A->",a)
print("value of B->",b)
#faster executoin then above 2 bcz its work on bit
a=a^b   
b=a^b	
a=a^b   


#below work on (ROT_TWO()) ::::The function swap the two top most item in stack
#a,b=b,a

print("********************************After swaping*****************************")
print("value of A->",a)
print("value of B->",b)


