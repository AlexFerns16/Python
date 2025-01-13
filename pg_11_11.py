# assignment one

dct = {
    'list1':[1, 2, 3, 4],
    'list2':[10, 20, 30, 40],
    'list3':[2, 4, 6, 8],
    'list4':[15, 25, 35, 45]
}


# method one : static
# ------------------------------------------------------------------------------------------

ind0=0; ind1=0; ind2=0; ind3=0

for i in dct.values():
    ind0 = ind0 + i[0]
    ind1 = ind1 + i[1]
    ind2 = ind2 + i[2]
    ind3 = ind3 + i[3]

lst = [ind0, ind1, ind2, ind3]
print(lst)


# method two : dynamic
# ------------------------------------------------------------------------------------------

lst = []
for i in dct.values():
    lst = lst + [i]
print(lst)

sumlst = []
for index in range(len(lst[0])):
    sumnum = 0
    for i in lst:
        sumnum = sumnum + i[index]
    sumlst = sumlst + [sumnum]
print(sumlst)
