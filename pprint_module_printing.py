""" it might be required to not just obtain the correct output, but get it in a neat, and presentable fashion. This is where pprint() method finds its significance. It helps print data objects in a pretty format, more readable, and well-formatted (pprint itself means pretty print).

For example, when the pprint method is used, data passed to this method is tried to be printed on a single line, and otherwise printed with indents on multiple lines. It needs to be imported before being used."""
"""The pprint module has a constructor called PrettyPrinter which has the below format:
"""
#class pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False)
"""
When this method is called, an instance of PrettyPrinter is created, which specifies the below values:

indent: The amount of indent when there are multiple lines

width: The amount of width between two data objects

depth: The number of levels which need to be printed

stream: An output stream (where the data is displayed) can be set-up

compact: It helps fit as many objects as possible within every line's width"""

#Syntax of pprint method
#pprint.pprint(object, stream=None, indent=1, width=80, depth=None, stream=None, *, compact=False, sort_dicts=True)

"""The object which needs to be printed in a well-formatted and readable fashion is passed to the pprint method of the pprint class. It prints the data and is followed by a newline. The other parameters like width, depth, compact and sort_dicts are passed to the PrettyPrinter constructor of the pprint class."""

import pprint

my_list={1:'rv',2:'Nik',3:'z', 4:'m', 5:'Studytonight'}
pprint.pprint(my_list,indent=1,width=40,depth=5,compact=2)

