# for loop patterns -----------------------


print()
# pattern 1 -------------------------------
for i in range(5+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()


print()
# pattern 2 -------------------------------

for i in range(5, 0, -1):
    for j in range(5, i-1, -1):
        print(j, end=' ')
    print()


print()
# pattern 3 -------------------------------

for i in range(5):
    for j in range(5, i, -1):
        print(j, end=' ')
    print()


print()
# pattern 4 -------------------------------

num = 5
# num = int(input('Enter the number of rows/cols: '))
for i in range(num+1):
    print((num-i) * ' ', end='')
    print(i * '* ', end='\n')


print()
# pattern 5 -------------------------------

num = 5
# num = int(input('Enter the number of rows/cols: '))
for i in range(num+1):
    print((num-i) * ' ', end='')
    if i < 3:
        print(i * '* ', end='\n')
    else:
        print('* ' + (i-2) * '  ' + '* ', end='\n')


print()
# pattern 6 -------------------------------

size = 7
# size = int(input('Enter the size of the pattern: '))
for row in range(size):
    for col in range(size):
        if col==size//2 or row==size//2 or (col==0 and row<=size//2) or (col==size-1 and row<=size//2):
            print('* ',end='')
        else:
            print('  ', end='')
    print()


print()
# pattern 7 -------------------------------

size = 7
# size = int(input('Enter the size of the pattern: '))
for row in range(size):
    for col in range(size):
        if row==0 or col==0 or (row==size-1) or (col==size-1) or (row==col) or (row+col==6):
            print('* ', end='')
        else:
            print('  ', end='')
    print()


print()
# pattern 8 -------------------------------

size = 7
for row in range(0, size):
    print(' ' * (size - row), end='')
    for col in range(65+row, 64, -1):
        print(chr(col), end='')
    print()


print()
# pattern 9 -------------------------------
for i in range(1, 5):
    print(' ' * (i-1), end = '')
    for j in range(i, 5):
        print(j, end = '')
    
    for k in range(3, i-1, -1):
        print(k, end = '')
    print()


print()
# pattern 10 -------------------------------
for i in range(1, 5+1):
    print(' ' * (5-i), end = '')
    for j in range(i):
        print((5+1)-i, end = '')
    print()

for i in range(1, 5+1):
    print(' ' * i, end = '')
    for k in range(5-i):
        print(i+1, end = '')
    print()


print()
# diamond
# pattern 11 -------------------------------

num=7
for i in range(1, num+1):
    for l in range(0, num-i):
        print(" ", end=" ")
    for m in range(0, i):
        print("*", end=" ")
    for n in range(0, i-1):
        print("*", end=" ")
    print()

for i in range(num-1, 0, -1):
    for l in range(0, num-i):
        print(" ", end=" ")
    for m in range(0, i):
        print("*", end=" ")
    for n in range(0, i-1):
        print("*", end=" ")
    print()


print()
# diamond with gap
# pattern 12 -------------------------------

num=5
for i in range(1, num+1):
    for l in range(0, num-i):
        print(" ", end=" ")
    for m in range(0, i):
        if m == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for n in range(0, i-1):
        if n == i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(num-1, 0, -1):
    for l in range(0, num-i):
        print(" ", end=" ")
    for m in range(0, i):
        if m == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for n in range(0, i-1):
        if n == i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#     5
#    44
#   333
#  2222
# 11111
#  2222
#   333
#    22
#     5
print()
# pattern 13 -------------------------------

num = 5
for i in range(num, 0, -1):
    for l in range(0, i-1):
        print(" ", end=" ")
    for m in range(0, num-i+1):
        print(i, end=" ")
    print()

for i in range(2, num+1):
    for l in range(0, i-1):
        print(" ", end=" ")
    for m in range(0, num-i+1):
        print(i, end=" ")
    print()

# 123454321
#  2345432
#   34543
#    454
#     5
print()
# pattern 14 -------------------------------
num = 5
num = num + 1
for i in range(1, num):
    for l in range(0, i-1):
        print(" ", end=" ")
    for m in range(i, num):
        print(m, end=" ")
    for n in range(num-2, i-1, -1):
        print(n, end=" ")
    print()

#     A
#    BA
#   CBA
#  DCBA
# EDCBA
print()
# pattern 15 -------------------------------
a = 65; b = 70
for i in range(a, b):
    for l in range(i, b-1):
        print(" ", end=" ")
    for m in range(i, 64, -1):
        print(chr(m), end=" ")
    print()
