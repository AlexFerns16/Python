print()
# --------------------------------------------------------------
def fun(arr):
    print(arr)

print()
fun([10, 20, 30])
fun((40, 50, 60))
fun({70, 80, 90})
fun({1:10, 2:20, 3:30})

print()
# --------------------------------------------------------------
def print_it(*args):
    print(args)             # args is a tuple
    print(*args)

print()
print_it(10, 20, 30)
print_it([10, 20], [30, 40])
print_it({'name':'abc', 'age':25})

tpl = (60, 70, 80)
print_it(tpl)
print_it(*tpl)

print()
# --------------------------------------------------------------
def print_it_itr(*args):
    print(args)
    print(*args)
    for i in args:              # args is a tuple
        print(i)


print_it_itr(10, 5.24, 8+2j, 'Python', True, b'\x41')

print()
# ----------------------------------------------
def print_x(u, v, w):
    print(u, v, w)

tpl_1 = (45, 55, 65)
tpl_2 = (47, 57, 67)
tpl_3 = (49, 59, 69)

print_x(*tpl_1)
print(*(45, 55, 65))
print(45, 55, 65)

print_x(*tpl_2)
print_x(*tpl_3)

print()
# ----------------------------------------------
def print_x(var):
    print(var)

tpl_1 = (45, 55, 65)
tpl_2 = (47, 57, 67)
tpl_3 = (49, 59, 69)

print_x(tpl_1)
print_x(tpl_2)
print_x(tpl_3)
