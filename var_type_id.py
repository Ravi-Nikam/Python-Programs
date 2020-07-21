a=1
b="f"
c=10.121212121212121212121212
d=1
x="sdsd"
print(type(a),id(a))
print(type(b),id(b))
print(type(c),id(c))

x=complex(c,d)
#y=complex(x,d)
print(type(x),id(x))
print(x.real,x.imag)
