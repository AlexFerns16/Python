# ----------------------------------------
# try:
#     a = 5
#     b = 7
#     c = a + b + d
# except NameError:
#     print('NameError Encountered')

# print('End of block')



# ----------------------------------------
try:
    a = int(input('Enter the value of a: '))
    b = int(input('Enter the value of b: '))
    # c = d + a / b                               # the first error encountered out of multiple errors in a statement is the respective exception thrown
except NameError:
    print('NameError Encountered')
except ZeroDivisionError:
    print('ZeroDivisionError Encounterd')

print('End of block')
