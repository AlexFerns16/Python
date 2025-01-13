# container types -------------------------------
# arrays
# list, tuple, set, and dictionary

# list > mutable and ordered collection
lst = [10, 20, 30, 40, 50]
print(lst[3])                   # accessing a list element
lst[3]=80                       # changing an element in a list
print(lst)

# tuple > immutable and ordered collection
tpl = (10, 20, 30, 40, 50)
print(tpl[3])                   # accessing a list element
# tpl[3]=80                     # cannot change and element in a tuple

# set > mutable and unordered collection
# set > cannot contain similar values
set_1 = {10, 20, 30, 40, 50}
set_2 = {40, 10, 30, 50, 20}
set_3 = {10, 20, 20, 30 ,50}

print(set_1)
print(set_2)
print(set_3)

# print(set_1[3])                 # cannot access individual element through indexing
# set_1[3]=80                     # cannot mutate through indexing

# dictionary > mutable and unordered collection
# key and value can be of any data type

x=10
dct_1 = {10:'A', 20:'B', 30:'C', 40:'D', 50:'E'}
dct_2 = {'A':2.56, 3+2j:4}
dct_3 = {10:(10, 20, 30), 'C':[40, 50, 60]}
dct_4 = {(10, 20, 30):'A', 'A':20}
dct_5 = {x:'ABC', 20:'DEF', 30:x}

# list, set, and dictionary being mutable will not work as a key in dictionary
# dct_6 = {[40, 50]:'A', (10, 20):'B'}
# dct_7 = {{40:'ABC'}:'A', (10, 20):'B'}
# dct_8 = {{10, 20}:'A', [40, 50]:40}

print(dct_1[20])
print(dct_2[3+2j])
print(dct_3['C'])
print(dct_4[(10, 20, 30)])
print(dct_5[x])
print(dct_5[30])
