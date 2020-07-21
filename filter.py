#filter only work with checking the condition

list1=[12,14,32,65,45]
list2=[21,41,22,6,25]

def age_check(age):
#    return (age*18)
    if age>18:
        return True
    else:
        return False


ans=filter(age_check,list1)
for i in ans:
    print(i)
