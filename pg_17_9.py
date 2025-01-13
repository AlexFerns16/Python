def display():
    a = 500
    print('This is the start of outer function')

    # inner function
    def show():
        print('This is the inner function')
        
        # global a        # a = 700
        # print(a)

        # nonlocal a      # a = 500
        # print(a)

        # a = 300         
        # print(a)        # a = 300

        print(a)          # a = 500

    show()
    print('This is the end of outer function')

a = 700
display()
