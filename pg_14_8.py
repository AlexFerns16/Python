# filter() -----------------------------

# --------------------------------------
lst_1 = ['A', 'X', 'Y', '3', 'M', '4', 'D']

f1 = filter(str.isalpha, lst_1)
print(list(f1))

# --------------------------------------
lst_2 = [5, 10, 18, 27, 25]

def fun(n):
    if n % 5 == 0:
        return True
    else:
        return False

f2 = filter(fun, lst_2)
print(list(f2))

# --------------------------------------
lst_3 = [[5], [10], [20, 30], [40, 50]]
f3 = filter(list.pop, lst_3)
print(list(f3))

# --------------------------------------
lst_4 = [5, 7, 5.25, 3+2j]

def fun_isinstance_one(var):
    if isinstance(var, int):
        return True
    else:
        return False

f4 = filter(fun_isinstance_one, lst_4)
print(list(f4))

# --------------------------------------
lst_5 = [10, 20, 5.24, 3+2j]

def fun_isinstance_two(var):
    if isinstance(var, int):
        return True
    else:
        return False

def filter_test(f, l):
    lst = []
    for i in l:
        if f(i):
            lst = lst + [i]
        else:
            pass
    return lst

f5 = filter_test(fun_isinstance_two, lst_5)
print(list(f5))
