print()
# example 1 -----------------------------------------------------
def fun_x(a, b=100, c=3.14):
    print(a+b+c)

fun_x(10)                 # passes '10' to 'a'
fun_x(10, 50)             # passes '10' to 'a', '50' to 'b'
fun_x(30, 60, 6.28)       # passes '30' to 'a', '60' to 'b', '6.28' to 'c'
fun_x(1, c=3, b=5)        # passes '1' to 'a', '5' to 'b', '3' to 'c'


print()
# example 2 -----------------------------------------------------
def fun_y(a, b, c, d, e):
    print(a, b, c, d, e)

lst = [10, 20, 30, 40, 50]
tpl = ('A', 'B', 'C', 'D', 'E')
s = {1, 2, 3, 4, 5}
 
fun_y(*lst)
fun_y(*tpl)
fun_y(*s)


print()
# example 3 -----------------------------------------------------
def fun_z(name='anil', marks='75'):
    print(name, marks)

dct = {'name':'amol', 'marks':50}

print()
fun_z(*dct)                             # *dct          >   'name', 'marks'

print()
fun_z(dct.keys())                       # dct.keys()    >   ['name', 'marks']
fun_z(dct.values())                     # dct.values()  >   ['amol', 50]
fun_z(dct.items())                      # dct.items()   >   [('name', 'amol'), ('marks', 50)]

print()
fun_z(**dct)                            # **dct         >   'amol', 50

print()
fun_z(*dct.keys())                       # dct.keys()    >   'name', 'marks'
fun_z(*dct.values())                     # dct.values()  >   'amol', 50
fun_z(*dct.items())                      # dct.items()   >   ('name', 'marks'), ('amol', 50)
