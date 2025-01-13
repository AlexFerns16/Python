# --------------------------------
def fun_one():
    a = 45
    print(a)
    print(id(a))

    def fun_two():
        a = 90
        print(a)
        print(id(a))

    fun_two()
    print(a)

fun_one()


# --------------------------------
def fun_one():
    a = 45
    print(a)
    print(id(a))

    def fun_two():
        # makes the changes in 'a' of 'fun_one' 
        nonlocal a
        a = 90
        print(a)
        print(id(a))

    fun_two()
    print(a)

fun_one()
