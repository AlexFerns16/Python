# --------------------------------------
try:
    a = int(input('Enter the value of a: '))
    b = int(input('Enter the value of b: '))
    c = a/b
    print(c)
except ZeroDivisionError:
    print('ZeroDivisionError Encountered')

print('End of block')



# --------------------------------------
# a = int(input('Enter the value of a: '))
# b = int(input('Enter the value of b: '))
# c = a/b
# print(c)
# print('next statement')
