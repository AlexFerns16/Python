# what are sets?

# --------------------------------------------------------
a = set()                       # empty set
print(a)

b = {20}                        # set with one element
print(b)

c = {'Sanjay', 25, 34555.50}    # set with multiple items
print(c)

d = {10, 10, 10, 10}            # only one 10 gets stored
print(d)

e = {}
print(type(e))

# --------------------------------------------------------
s = {12, 23, 45, 16, 52}    # insertion order
t = {16, 52, 12, 23, 45}    # insertion order
u = {52, 12, 16, 45, 23}    # insertion order
print(s)    # accesing order is dependent on the hash value of the element
print(t)    # accesing order is dependent on the hash value of the element
print(u)    # accesing order is dependent on the hash value of the element

# --------------------------------------------------------
s1 = {'Morning', 'Evening'}
s2 = {(12, 13), (15, 25), (17, 34)}
# s3 = {[12, 23], [15, 25], [17, 34]}     
# since a list may change its hash value, 
# a list is not permitted in a set
# a set cannot contain mutable objects

# note: ----------------------------------------------------
# sets cannot be accessed using indexing
# sets cannot be sliced using indexing
