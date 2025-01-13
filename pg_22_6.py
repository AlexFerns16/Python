try:
    a = int(input('Enter the value of a: '))
    b = int(input('Enter the value of b: '))
    c = a / b
    print(c)
except:
    print('This is an exception')
else:
    print('No exceptions')

# the else block goes to work when no exceptions occur
