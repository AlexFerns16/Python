lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

b = []
for i in lst:
    a = []
    for j in i:
        a = a + [j+1]
    b = b + [a]
print(b)

for index_outer, element in enumerate(lst):
    for index_inner in range(0, len(element)):
        lst[index_outer][index_inner] = lst[index_outer][index_inner] * 10
print(lst)
