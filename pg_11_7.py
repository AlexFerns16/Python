
# ---------------------------------------------------------------------------
c = {'CS101':'OOP', 'CS102':'DS', 'CS201':'CPP'}
d = {'ME126':'HPE', 'ME102':'TOM', 'ME234':'AEM'}

print(c.get('CS102', 'Absent'))
print(c.get('EE102', 'Absent'))
# print(c['EE102'])                 # raises key error


# ---------------------------------------------------------------------------
dct = {2: 20, 5: 50, 9: 90}

# output > dct = {2: 20, 5: 50, 9: 90, 1: 'A', 3: 'A', 4: 'A', 6: 'A', 7: 'A', 8: 'A', 10: 'A'}

for key in range(1, 11):
    dct[key] = dct.get(key, 'A')
print(dct)


# ---------------------------------------------------------------------------
# update
c.update(d)
print(c)

# copy - creating a new object
e = c.copy()
print(e)

# copy - copying the same address
f = c
print(f)

print(c.popitem())
print(c)


# reversing a dictionary
# ---------------------------------------------------------------------------
dct_one = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dct_one = 
# dct_two = 

dct_two = {}
for count in range(3):
    tpl = dct_one.popitem()
    dct_two[tpl[0]] = tpl[1]
print(dct_one)
print(dct_two)


# ---------------------------------------------------------------------------
print(c.pop('CS102'))
print(c)

# clearing the elements of a dictionary
c.clear()
print(c)

# deleting the entire dictionary
del(c)
# print(c)


# ---------------------------------------------------------------------------

# remove the items where a certain value is occuring more than once
d = {'x':10, 'y':20, 'z':30, 'u':10, 'v':20, 'w':40}
e = d.copy()

lst = []
for key1, val1 in e.items():
    if val1 not in lst:
        lst = lst + [val1]
    else:
        for key2, val2 in e.items():
            if val2 == val1:
                d.pop(key2)
print(d)


# ---------------------------------------------------------------------------

# remove the repeated items where a certain value is occuring more than once
d = {'x':10, 'y':20, 'z':30, 'u':10, 'v':20, 'w':40, 'a':10, 'b':50, 'c':30}
e = d.copy()

lst = []
for key1, val1 in e.items():
    if val1 not in lst:
        lst = lst + [val1]
    else:
        for key2, val2 in e.items():
            if val2 == val1:
                if key2 in d.keys():
                    d.pop(key2)
                    break
print(d)
