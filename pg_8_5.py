# using built-in functions on lists

lst1 = [10, 20, 30, 40, 50]
lst2 = [60, 0, 70, -80, 90]
lst3 = [0, 0, 0, 0, 0]

print()
# length ---------------------------------------------
print(len(lst1))
print(len(lst2))
print(len(lst3))

print()
# max ---------------------------------------------
print(max(lst1))

print()
# min ---------------------------------------------
print(min(lst1))

print()
# sum ---------------------------------------------
print(sum(lst1))

print()
# any > returns 'True' if any element of the list is 'True'
print(any(lst1))
print(any(lst2))
print(any(lst3))

print()
# all > returns 'True' if all elements of the list are True
print(all(lst1))
print(all(lst2))
print(all(lst2))

print()
# del > deletes element or slice or entire list

# code 1 -------------------------------------------------

print()
lst4 = [10, 20, 30, 40, 50]
print(lst4)
del(lst4)                       # del() > deletes the entire list: memory location gets deleted
# print(lst4)

print()
lst5 = [10, 20, 30, 40, 50]
print(lst5)
lst5[:] = []
print(lst5)

print()
lst6 = [60, 70, 80, 90, 100]
print(lst6)
del(lst6[2:5])
print(lst6)

print()
lst7 = [60, 70, 80, 90, 100]
print(lst7)
lst7 = []
print([])

# code 2 -------------------------------------------------

lst1 = [10, 20, 30, 40, 50]
lst3 = lst2 = lst1
lst1 = []
print(lst1)
print(lst2)
print(lst3)

# code 3 -------------------------------------------------

lst1 = [10, 20, 30, 40, 50]
lst3 = lst2 = lst1
lst1[1:3] = []
print(lst1)
print(lst2)
print(lst3)

# example 1 ----------------------------------------------
lst1 = [10, 20, 50, 40, 30]
lst2 = [10, 20, 50, 40, 30, 60]

def max_num_func(lst):
    max_num = 0
    for var in lst:
        if max_num > var:
            max_num = max_num
        else:
            max_num = var
    print(max_num)

print(max_num_func(lst1))
print(max_num_func(lst2))

# example 2 ----------------------------------------------
lst1 = [10, 20, 50, 40, 30]
lst2 = [10, 20, 50, 40, 30, 5]

def min_num_func(lst):
    min_num = lst[0]
    print(min_num)
    for var in lst:
        if min_num > var:
            min_num = var
        else:
            min_num = min_num
    print(min_num)

print(min_num_func(lst1))
print(min_num_func(lst2))

# example 3 ----------------------------------------------
lst1 = [0, 0, 50, 0, 0]
lst2 = [0, 0, 0, 0, 0]

def any_func(lst):
    global var
    for var in lst:
        if var:
            var = True
            break
        else:
            var = False

any_func(lst1)
print(var)

any_func(lst2)
print(var)

# example 4 ----------------------------------------------
lst1 = [10, 20, 30, 40, 50]
lst2 = [10, 20, 0, 40, 50]

def all_func(lst):
    global var
    for var in lst:
        if var:
            continue
        else:
            var = False
            break
    else:
        var = True

all_func(lst1)
print(var)

all_func(lst2)
print(var)
