try:
    a = int(input('Enter the value of a: '))
    b = int(input('Enter the value of b: '))
    c = a / b
    print(c)
except:
    print('This is an exception')
finally:
    print('I am finally')

# the finally block goes to work even when the exception is executed
