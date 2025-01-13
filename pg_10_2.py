# looping in sets

s = {12, 15, 13, 23, 22, 16, 17}
print(s)

for ele in s:
    print(ele)

for ind, ele in enumerate(s):
    print(ind, ele)



# example --------------------------------------

#
x = []
for i in s:
    x = x + [i]
print(x)

# [(0, 16), (1, 17), (2, 22), (3, 23), (4, 12), (5, 13), (6, 15)]
lst = []; count = 0
for element in s:
    lst = lst + [(count, element)]
    count = count + 1
print(lst)
