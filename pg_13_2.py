# global function: fun1()
def fun1():
    print('start of fun1')
    print('This is fun1 before defining fun2')
    # local function: fun2()
    def fun2():
        print('This is start of fun2')
        print('This is fun2')
        print('This is end of fun2')
    print('This is fun1 after defining fun2')
    # fun2()
    print('This is end of fun1')

# --------------------
# fun1()
# print(type(fun1))
