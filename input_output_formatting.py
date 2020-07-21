                                                #The actual syntax of the print() function is
"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Here, objects is the value(s) to be printed.

The sep separator is used between the values. It defaults into a space character.

After all values are printed, end is printed. It defaults into a new line.

The file is the object where the values are printed and its default value is sys.stdout (screen). Here are an example to illustrate this."""


print(1,2,3,4,sep="#",end="^")
print('h','e','l','l','o',sep="#")


                                                    #Output formatting

"""Sometimes we would like to format our output to make it look attractive.
This can be done by using the str.format() method. This method is visible to any string object."""

x=5
y=10
print("\nTHE VALUE OF X IS {} AND Y IS {}".format(x,y))

"""Here the curly braces {} are used as placeholders. We can specify the order in which it is printed by using numbers (tuple index)."""

print('I LOVE {0} AND {1}'.format('bread','butter'))

                                    #keyword arguments to format the string
"""We can even use keyword arguments to format the string."""
print('Hello{name},{gratting}'.format(name="rv",gratting="gm"))

"""We can even format strings like the old sprintf() style used in C programming language. We use the % operator to accomplish this."""

x=1295.12133234
print("FLoat value is %2.4f"%x)

                                #input in python
num = input('Enter a number: ')
print(num)


# f'  only work in gre version 3.6 , 3.7 of py
message3=f'{x},{y},'
print(message3)
