# dictionary varieties

print()
# variety 1 ------------------------------------
d = {(1, 5):'ME126', (3, 2):'ME102', (5, 4):'ME234'}

print()
# variety 2 ------------------------------------
contacts = {
    'Anil':{'DOB':'17/11/98', 'Favorite':'Igloo'},
    'Amol':{'DOB':'14/10/99', 'Favorite':'Tundra'},
    'Ravi':{'DOB':'19/11/97', 'Favorite':'Artic'}
}
print(contacts['Anil']['Favorite'])

# method 1 ------------------
tpl=()
for i in contacts.values():
    print(i)
    tpl=tpl+((i['DOB'], i['Favorite']),)
print(tpl)

# method 2 ------------------
tpl=()
for i in contacts.values():
    print(i)
    tpl=tpl+((tuple(i.values())),)
print(tpl)

print()
# variety 3 ------------------------------------
animals = {'Tiger':141, 'Lion':152, 'Leopard':110}
birds = {'Eagle':38, 'Crow':3, 'Parrot':2}

combined = {**animals, **birds}
print(combined)

print()
# variety 4 ------------------------------------
lst = [12, 13, 14, 15, 16]
d = dict.fromkeys(lst, 25)
print(d)

# using for loop
dct = {}
for i in lst:
    dct[i] = 25
print(dct)

# --------------------------------
lst1 = [10, 20, 30]
lst2 = [100, 200, 300]

dct = {}
for i in range(len(lst1)):
    dct[lst1[i]] = lst2[i]
print(dct)

# --------------------------------
tpl = (60, 50, 40)

dct = {}
for i, a in enumerate(tpl):
    dct = {**dct, **{i:a}}
print(dct)

# --------------------------------
lst1 = [10, 20, 30]
lst2 = [100, 200, 300]

dct_x = {}
# method 1 -----------------
for i, j in zip(lst1, lst2):
    dct_x[i] = j
print(dct_x)

# method 2 -----------------
print(dict(zip(lst1, lst2)))

# other --------------------
print(list(zip(lst1, lst2)))

# --------------------------
contacts['Anil'].pop('Favourite')
