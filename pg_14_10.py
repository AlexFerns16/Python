# lambda with map(), filter(), reduce() ------------------------

# using lambda with map() --------------------------------------
lst_1 = [5, 10, 15, 20, 25]
m = map(lambda n : n * n, lst_1)
print(list(m))

# using lambda with filter() -----------------------------------
lst_2 = [5, 10, 18, 27, 25]
f = filter(lambda n : n % 5 == 0, lst_2)
print(list(f))

# using lambda with reduce() -----------------------------------
from functools import reduce
lst_3 = [1, 2, 3, 4, 5]
s = reduce(lambda x, y : x + y, lst_3)
p = reduce(lambda x, y : x * y, lst_3)
print(s, p)
