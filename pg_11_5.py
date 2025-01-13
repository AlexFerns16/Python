# concatenation - doesn't work
# merging - doesn't work
# conversion - works
# aliasing - works
# cloning - doesn't work
# searching - works
# identity - works
# comparison - not very sure, but it doens't work as expected
# emptiness - works

print()
# concatenation -------------------------
# dct_1 = {1:10, 2:20, 3:30}
# dct_1 = dct_1 + {4:40, 5:50}
# print(dct_1)

print()
# merging -------------------------
# dct_1 = {1:10, 2:20, 3:30}
# dct_2 = {4:40, 5:50}
# dct_3 = dct_1 + dct_2
# print(dct_3)

print()
# conversion -------------------------
dct_1 = {1:10, 2:20, 3:30}
print(list(dct_1.keys()))
print(list(dct_1.values()))
print(list(dct_1.items()))

print()
# aliasing -------------------------
dct_1 = {1:10, 2:20, 3:30}
dct_2 = dct_1
print(dct_2)

print()
# cloning -------------------------
# dct_1 = {1:10, 2:20, 3:30}
# dct_2 = {} + dct_1
# print(dct_2)

print()
# searching -------------------------
dct_1 = {1:10, 2:20, 3:30}
print(1 in dct_1.keys())
print(10 in dct_1.values())
print((1, 10) in dct_1.items())

print()
# identity ---------------------------
dct_1 = {1:10, 2:20, 3:30}
dct_2 = dct_1                   # address of dct_1 is copied to dct_2
dct_3 = {1:10, 2:20, 3:30}      # new object is created
print(dct_1 is dct_2)
print(dct_1 is dct_3)

print()
# comparison ---------------------------
dct_1 = {1:10, 2:20, 3:30}
dct_2 = {1:10, 2:20, 3:30}
print('comparision')
print(dct_1.keys() == dct_2.keys())
print(dct_1.values() == dct_2.values())
print(dct_1.items() == dct_2.items())
# print(dct_1 > dct_2)
# print(dct_1 < dct_2)

print()
# emptiness ---------------------------
dct_1 = {1:10, 2:20, 3:30}
dct_2 = {}

if dct_1:
    print('Full')

if not dct_2:
    print('Empty')


# --------------------------------------------------------------------

dct1 = {'x':10, 'y':20, 'z':30}
dct2 = {'m':40, 'n':50, 'o':60}

lst = list(dct2.items())
dct = {}

for ind, (key, val) in enumerate(dct1.items()):
    dct[key + '+{}'.format(lst[ind][0])] = val + lst[ind][1]
    
print(dct)
