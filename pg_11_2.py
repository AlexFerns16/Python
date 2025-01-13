# accessing dictionary elements

# dictionaries preserve insertion order
d1 = {'A101':'Amol', 'A102':'Anil', 'B103':'Ravi'}

for ind, ele in enumerate(d1):
    print(ind, ele)

# elements are not position indexed, but key indexed
print(d1['A102'])

# using tuple as a key is permitted
d2 = {(10, 20):'Amol', 'A102':'Anil', 'B103':'Ravi'}
print(d2[(10, 20)])

# using list as a key is not permitted, because list is mutable/unhashable
# the following statement will result in error
# d3 = {[10, 20]:'Amol', 'A102':'Anil', 'B103':'Ravi'}
# print(d3[[10, 20]])
