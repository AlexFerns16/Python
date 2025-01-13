try:
    x = int('abc')
    print(x)
except ValueError:
    print('This is a ValueError')
except:
    print('OtherExceptions')
