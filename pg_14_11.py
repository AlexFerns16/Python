# map(), filter(), reduce() together ----------------------

# ---------------------------------
import math
lst = [5, 10, 15, 20, 25]
x = map(lambda n : round(n, 2), map(math.radians, lst))
print(list(x))

# ---------------------------------
def fun(n):
    return n > 1000

lst = [10, 20, 30, 40, 50]
l = filter(fun, map(lambda x : x * x, lst))
print(list(l))
