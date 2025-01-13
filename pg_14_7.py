# map() -------------------------------

# -------------------------------------
import math

lst = [5, 10, 15, 20, 25]

m1 = map(math.radians, lst)
print(list(m1))

m2 = map(math.factorial, lst)
print(list(m2))

# -------------------------------------
def fun(n):
    return n * n

m3 = map(fun, lst)
print(list(m3))

# example 1 ---------------------------
lst = [10, 20, 30, 40, 50]

def map_test(x, l):
    lst = []
    for i in l:
        lst = lst + [x(i)]
    return lst

var = map_test(math.radians, lst)
print(var)
