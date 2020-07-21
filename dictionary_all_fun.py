#Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key: value pair.
#keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.

# empty dictionary
my_dict = {}
# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}


# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

"""While indexing is used with other container types to access values, dictionary uses keys. Key can be used either inside square brackets or with the get() method.

The difference while using get() is that it returns None instead of KeyError, if the key is not found."""

print("using []",my_dict[1])
print("using get()",my_dict.get(4))

my_dict[1]='applesss'
print("using assigning values:",my_dict[1])

my_dict['address']='banana'
print("Adding values:",my_dict)

#We can also use the del keyword to remove individual items or the entire dictionary itself.
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print("remove item using pop key 4",squares.pop(4))
print(squares)

print("pop item",squares.popitem())

del squares[2]
print("delete particular item",squares)
del squares #remove whole dictionary

#Return a new dictionary with keys from seq and value equal to v

my={}.fromkeys(['ma','y','n'],2)
print(my)

for my in my:
    print(my)

#sorted
#print(list(sorted(my.keys())))

squares = {x: x*x for x in range(6)}

print(squares)




