print()
# example 1 --------------------------------------------------
# def refact(n):
#     if n == 0:
#         return 1
#     else:
#         p = n * refact(n-1)
#     return p

# num = 5
# fact = refact(num)
# print('factorial value: ', fact)


print()
#  example 2 --------------------------------------------------
def sq_lst(var):
    lst = []
    for i in var:
        lst = lst + [i**2]
    return lst

lst_1 = [10, 20, 30]
print(sq_lst(lst_1))



print()
#  example 3 --------------------------------------------------
def sq_lst(var):
    lst = []
    for i in var:
        if isinstance(i, int):
            lst = lst + [i**2]

        if isinstance(i, list):
            x = sq_lst(i)
            lst = lst + [x]
    return lst

lst_1 = [10, 20, 30, [40, 50, 60]]
print(sq_lst(lst_1))
