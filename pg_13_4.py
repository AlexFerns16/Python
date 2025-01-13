# positional arguments
def fun(i, j, k):
    print(i+j)
    print(k.upper())

fun(10, 20, 'Python')
# fun('Python', 10, 20)     # error

# keyword arguments
def fun(i, j, k):
    print(i, j, k)

fun(i=10, j=15.45, k='Python')
fun(j=17.45, k='CPython', i=20)
fun(10, k='Jython', j=14.45)
# fun(k='Jython', j=14.45, 10)        # positional argument follows keyword argument
# fun(10, i='Jython', j=14.45)        # multiple value of argument 'i'
