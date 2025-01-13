# tuple variations

# --------------------------------------------
a = (1, 3, 5, 7, 9)
b = (2, 4, 6, 8, 10)
c = (a, b)
print(c[0][0], c[1][2])

# --------------------------------------------
records = (
    ('abc', 24, 1.23), ('def', 25, 1.24),
    ('ghi', 26, 1.25), ('jkl', 27, 1.26)
)

print()
print(records[1][2])

print()
for ele in records:
    print(ele)

print()
for a, i, f in records:
    print(a, i, f)

print()
for ele in records:
    print(ele[0], ele[1], ele[2])

# --------------------------------------------
file = (
    ('abc', (24, 25), 1.23), ('def', (26, 27), 1.24),
    ('ghi', (28, 29), 1.25), ('jkl', (21, 22), 1.26)
)

print()
for ele in file:
    print(ele)

print()
for a, i, f in file:
    print(a, i, f)

print()
for a, i, f in file:
    print(a, i[1], f)

print()
for ele in file:
    print(ele[0], ele[1][1], ele[2])

# --------------------------------------------
x = (1, 2, 3, 4)
y = (10, 20, x, 30)
print(y)

# --------------------------------------------
x = (1, 2, 3, 4)
y = (10, 20, *x, 30)
print(y)

# --------------------------------------------
lst = [('abc', 24, 1.23), ('def', 25, 1.24)]    # creating tuples in a list
tpl = (['abc', 24, 1.23], ['def', 25, 1.24])    # creating lists in a tuple

# lst[0][1] = 27                                # tuple inside a list cannot be mutated
# print(lst)

tpl[0][1] = 27                                  # list inside a tuple can be mutated
print(tpl)

# --------------------------------------------

# method 1 -----------------------------------
names = ['abc', 'def', 'ghi', 'jkl', 'mno']
ages = [15, 25, 35, 20, 13]
marks = [10, 15, 19, 16, 13]

for i in names, ages, marks:
    for j in i:
        print(j, end=' ')
    print()

# method 2 -----------------------------------
lst = [names, ages, marks]

for i in lst:
    for j in i:
        print(j, end=' ')
    print()

# example 1 ---------------------------
records = (
    ('abc', 24, 1.23), ('def', 25, 1.24),
    ('ghi', 26, 1.25), ('jkl', 27, 1.26)
)

# method 1 -----------------------------
lst = []
for i in records:
    lst = lst + [[*i]]
print(lst)

# method 2 -----------------------------
lst_out = []
for i in records:
    lst_inn = []
    for j in i:
        lst_inn = lst_inn + [j]
    lst_out = lst_out + [lst_inn]
print(lst_out)

# example 2 ---------------------------
import random

lst = []
while len(lst) <= 9:
    x = random.randint(1, 10)
    if x in lst:
        pass
    else:
        lst.append(x)
        print(x)
print(lst)
