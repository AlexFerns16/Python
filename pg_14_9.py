# reduce() -------------------------------

# ------------------------------------
from functools import reduce
lst = [1, 2, 3, 4, 5]

# ------------------------------------
def getsum(x, y):
    return x + y

s = reduce(getsum, lst)
print(s)

# ------------------------------------
def getprod(x, y):
    return x * y

p = reduce(getprod, lst)
print(p)
