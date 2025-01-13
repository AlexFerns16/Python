try:
    a = int(input('Enter the value of a: '))
    b = int(input('Enter the value of b: '))
    c = a / b
    print('c = ', c)
except ZeroDivisionError as zde:
    print(zde)
    print(zde.args)
