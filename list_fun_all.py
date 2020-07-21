my_list=['r','v','n','i','k','a','m']
print(my_list) #print all list
print(my_list[0:5:1])#0 to 5 print with 1 incrment
n_list=["Hello",[1,2,3,4,['r','v']]]#nested list 
print(n_list[1][4][0])

print(my_list[0:-2:2]) #nagtive indexing
print(n_list[-1][-1][-1])
print(len(n_list[1][4])) #nested length function 

xyz=['ra','a','n','i']

#SLICING

my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[2:5]) #op:-[o,g,r]

print(my_list[1:-5])
print(my_list[2:])
print(my_list)
my_list[2:4]=['r','v'] #assigning values in list
print("assigning values in list",my_list)

my_list.append(6)
print(my_list)
my_list.extend([12,12,3])
print(my_list)

"""We can also use + operator to combine two lists. This is also called concatenation.

The * operator repeats a list for the given number of times."""
xy=['nikam','rv'];
print(my_list+['nikam','rv']) #concating value in list
print(xy*3*2+[2])#concat and repeting values in list

print("my",my_list)
print(my_list.insert(1,"skdksd"))
print(my_list)

my_list[4:9]=[32,43]
print("Add values multiple",my_list)

#We can delete one or more items from a list using the keyword del. It can even delete the list entirely.

print(my_list)
del my_list[1:6]
print("deleting list",my_list)

#delete entire list
#del my_list


#We can use remove() method to remove the given item or pop() method to remove an item at the given index.
#The pop() method removes and returns the last item if index is not provided.
#We can also use the clear() method to empty a list.

print(my_list)
my_list.remove('z')
print("remove",my_list)

my_list.pop(2)
my_list.pop()
print("pop",my_list)

#my_list.clear()
#print("Clear",my_list)

#we can also delete items in a list by assigning an empty list to a slice of elements
#my_list[1:3]=[]
print("delete items in a list by assigning an empty list",my_list)

#The count() method returns the number of occurrences of an element in a list.

print("count no of items present in list",my_list.count('p'))
xyz.sort()
print("sort",xyz)
xyz.sort(reverse=True)
print("Sorted list (in Descending)",xyz)


#The sort() method sorts the elements of a given list in a specific order - Ascending or Descending.
#Alternatively, you can also use Python's in-built function sorted() for the same purpose
#Simplest difference between sort() and sorted() is: sort() doesn't return any value while, sorted() returns an iterable list.
#By default, sort() doesn't require any extra parameters. However, it has two optional parameters:
#reverse - If true, the sorted list is reversed (or sorted in Descending order)
#key - function that serves as a key for the sort comparison



"""Here, len is the Python's in-built function to count the length of an element.

The list is sorted based on the length of its each element, from lowest count to highest."""

xyz.sort(key=len)
print("sorting using len function",xyz)



#index() - Returns the index of the first matched item

print("firsr match index ",my_list.index('p'))


#List comprehension is an elegant and concise way to create a new list from an existing list in Python.
for i in range(10):
    print(i)
pow2 = [2 ** x for x in range(10)]
print(pow2)

#OR

pows = []
for x in range(10):
   pows.append(2 ** x)


#pow > 5
pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

#odd values
odd = [x for x in range(20) if x % 2 == 1]
print(odd)

#[x+y for x in ['Python ','C '] for y in ['Language','Programming']]    







