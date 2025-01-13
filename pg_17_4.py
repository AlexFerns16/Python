# outer function
def display():
    a = 500
    print('This is the start of outer function')

    # inner function
    def show():
        print('This is the inner function')
        print(a)

    show()
    print('This is the end of outer function')

display()
