string = "123456789987654321"
for strin in string:
    print(strin)


my_iterator = iter(string)
print("give memory location of first value it not give value of it",my_iterator)


# The __next__() method also allows you to do operations, and must return the next item in the sequence.
print(next(my_iterator))
print(next(my_iterator))


# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
for char in iter(string):
    print(char)
    


my_list=['mon','Tue','wen','Thus','Fri','sat']

my_val = iter(my_list)

for char in range(0,len(my_list)):
    next_iter  = next(my_val)
    print(next_iter)
