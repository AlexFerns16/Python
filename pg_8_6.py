# list methods
# lst.methods()

lst = [12, 15, 13, 13, 23, 22, 16, 17]
print(lst)

# add new item at end
lst.append(22)
print(lst)

# delete item 13 from list
lst.remove(13)
print(lst)
 
# reports ValueError as 30 is absent in lst
# print(lst.remove(30))

# removes the last item from the list
lst.pop()
print(lst)

# removes 3rd item from the list
lst.pop(3)
print(lst)

# insert 21 at 3rd position
lst.insert(3, 21)
print(lst)

# returns number of times 21 appears in list
print(lst.count(21))

# return index of item 22
idx = lst.index(22)
print(idx)
# idx = lst.index(50)
# print(idx)            # error > ValueError as 50 is absent in list


# examples -------------------------------------------------------------------

# code 1 ------------------------------------------

lst_a = [10, 20, 30, 30, 40, 50, 30, 60]
x = tuple(lst_a)
# using a copy of list in tuple for reference, 
# since the original list will tend to change the index positions of elements,
# while lst_a.remove() is operated.

# method 1
for i in x:
    if i==30:
        lst_a.remove(30)
print(lst_a)

# method 2
lst_a = [10, 20, 30, 30, 40, 50, 30, 60]
for i in range(0, lst_a.count(30)):
    lst_a.remove(30)
print(lst_a)


# code 2 ------------------------------------------

list_1 = [10, 20, 30]
list_2 = [40, 50, 60]

list_3 = list_2 + [list_1.pop()]
print(list_3)

list_2 = list_2 + [list_1.pop()]
list_2.insert(1, list_1.pop(0))
print(list_1)
print(list_2)
