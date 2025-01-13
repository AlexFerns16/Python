print()
# ----------------------------------
a = 20
b = 3.14
s = 'Python'
lst = ['a', 'b', 's']
for var in lst:
    print(globals()[var])

print()
# ----------------------------------
def fun_one():
    print('inside fun_one')

def fun_two():
    print('inside fun_two')

def fun_three():
    print('inside fun_three')

lst = ['fun_one', 'fun_two', 'fun_three']

for var in lst:
    globals()[var]()

    # if globals()[var]() != None:
    #     print('', end='')
