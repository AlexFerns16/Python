# built-in functions on dictionaries

d = {'CS101':'OOP', 'CS102':'DS', 'CS201':'CPP'}
d1 = {'CS101':0, 'CS102':1, 'CS201':0}

# len(d) ----------------------------------------
pass

# max(d) ----------------------------------------
print(max(d.keys()))
print(max(d.values()))
print(max(d.items()))       # comparing the first value in each tuple

# min(d) ----------------------------------------
pass

# sorted(d) -------------------------------------
sorted(d)
print(sorted(d))
print(sorted(d.values()))
print(sorted(d.items(), reverse=True))

# sum(d) ----------------------------------------
# will work only with numbers

# any() -----------------------------------------
print(any(d))
print(any(d1.values()))

# all() -----------------------------------------

# reversed(d) -----------------------------------
print(list(reversed(d.items())))

# examples --------------------------------------

# sorting a dictionary by values without using sorted()/sorted(reverse)/reversed()
# lst=[]
# for k, v in d.items():
#     lst = lst + [(k, v)]
# print(lst)

# import operator
# sor = sorted(lst, key=operator.itemgetter(1))
# print(sor)

# dct = {}
# for i in range(len(sor)):
#     dct[sor[i][0]] = sor[i][1]
# print(dct)

# use of reversed() in for loop
# for k, v in reversed(d.items()):
#     print(k, v)

# for k, v in reversed(d.values()):
#     print(k, v)

# # use of sorted() in for loop
# for i in sorted(d.values()):
#     print(i) 

# insertion method example ------------------------
d = {1: 6, 2: 4, 3: 5, 4: 8}
A = list(d.items())
for i in range(1, len(d)):
    j = i
    while j > 0 and A[j-1][1] > A[j][1]:
        A[j], A[j-1] = A[j-1], A[j]
        j -= 1
print(dict(A))

# bubble sort method example ------------------------
d = {1: 6, 2: 4, 30: 5, 4: 8}
A = list(d.items())
for i in range(len(A)):
    for j in range(0, len(A)-i-1):
        if A[j][1] > A[j+1][1]:
            A[j], A[j+1] = A[j+1], A[j]
print(dict(A))
