# assigning a function to a variable
# and calling a function using the variable

# example 1 ---------------------------------------------
def func():
    print('Hello')

def sum(x, y):
    print(x+y)

f = func                # assigning function 'func()' to a variable 'f'
f()                     # this is a call to function 'func()'

g = sum                 # assigning function 'sum()' to a variable 'g'
g(10, 20)               # this is a call to function 'sum(x, y)'
