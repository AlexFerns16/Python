# basic set operations

s = {'gate', 'fate', 'late'}
s.add('rate')
print(s)

# s = frozenset({'gate', 'fate', 'late'})
# s.add('rate')
# print(s)

# concatenation - doesn't work
# merging - doesn't work
# conversion - works
# aliasing or shallow copy - works
# cloning or deep copy - doesn't work
# searching - works
# identity - works
# comparison - not sure
# emptiness - works


# examples --------------------------------

# example 1 -------------------------------

s1 = {10, 20, 30}
s2 = s1
print(s2)
print(id(s1))
print(id(s2))

# s1 = {10, 20, 30}
# s2 = set() + s1
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))

s3 = {10, 20, 30}
s4 = {40, 50, 60}
print(s3 is s4)

s5 = {10, 20, 30}
print(s5)
s6 = {10, 20, 30}
print(s5)
print(s5 == s6)

s5 = {10, 30, 40, 50}
print(s5)
s6 = {10, 20, 30}
print(s6)
# True > if all the elements of s6 are contained in s5
print(s5 > s6)

# example 2 -------------------------------

tpl=()
s = {12, 13, 14, (15, 16), (17, 18)}
for i in s:
    if isinstance(i, tuple):
        tpl=tpl+(*i,)
    else:
        tpl=tpl+(i,)
print(tpl)

# example 3 -------------------------------

set_s=set()
s = {12, 13, 14, (15, 16), (17, 18)}
for i in s:
    if isinstance(i, tuple):
        for j in i:
            set_s.add(j)
    else:
        set_s.add(i)
print(set_s)

# example 4 -------------------------------

s = {5, 7, 8, (10, 8), (9, 7)}

tpl_one = ()
for i in s:
    if isinstance(i, int):
        tpl_one = tpl_one + (i**2,)
    tpl_two = ()
    if isinstance(i, tuple):
        for j in i:
            tpl_two = tpl_two + (j**2,)
        tpl_one = tpl_one + (tpl_two,)
print(tpl_one)

# example 5 -------------------------------

s = {5, 7, 8, (10, 8), (9, 7)}

set_one = set()

for i in s:
    if isinstance(i, int):
        set_one.add(i**2)
    tpl_two = ()
    if isinstance(i, tuple):
        for j in i:
            tpl_two = tpl_two + (j**2,)
        set_one.add(tpl_two)
print(set_one)
