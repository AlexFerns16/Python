# address of an objects variable

a = 10
b = 10
c = a + b
print(c)
print(id(a))
print(id(b))
print(id(c))


d=4
e=4
print(id(d))                    # id() > gives the address of an objects variable 'd'
print(id(e))                    # id() > gives the address of an objects variable 'e'
