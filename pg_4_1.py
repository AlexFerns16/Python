# program_1 ---------------------------------------------------
print()

s = 'I Am Superman'
t = s.split(' ')
print(t)

# program_2 ---------------------------------------------------
print()

u = 'I Am A Legend'.split(' ')
print(u)

# program_3 ---------------------------------------------------
print()

lst = input('Enter list: ').split(' ')
print(lst)

s='Hello'

t=" ".join(s)
print(t)

u=t.split(' ')
print(u)

i=".".join(s)
print(i)

j=i.split('.')
print(j)
'' ' '
# program_4 --------------------------------------------------
print()

msg_1 = 'He said, Let us Python'
print(msg_1)

msg_2 = 'He said, \'Let us Python\''
print(msg_2)

msg_3 = "He said, 'Let us Python'"
print(msg_3)

msg_4 = 'He said, "Let us Python"'
print(msg_4)


# program_5 --------------------------------------------------
print()

#  -5  -4  -3  -2  -1       # index position
#   H   e   l   l   o
#   0   1   2   3   4       # index position

strg = 'Hello'

print(strg)
print(strg[1])
print(strg[:3])
print(strg[2:])
print(strg[2:4])
print(strg[-4:-1])
print(strg[1:-1])
print(strg[2:100])            # prints till the end of the string
# print(strg[100])            # error, 100th element does not exist

# program_6 --------------------------------------------------
print()

# string properties

stg_1 = 'Python'
print(stg_1)
# stg_1[0] = 'M'                        # string is immutable
stg_1 = 'CPython'
print(stg_1)

print('/' * 10)                         # string replication

print('name' + ' ' + 'surname')         # string concatenation

print('e' in 'Hello')
print('ll' in 'Hello')
print('lol' in 'Hello')
print('z' in 'Hello')

# built-in functions -------------------------

stg_2 = 'Jython'
print(len(stg_2))
print(min(stg_2))
print(max(stg_2))

# string methods -----------------------------

stg_3 = 'PyPy'
print(type(stg_3))              # data types
print(id(stg_3))                # address

import random                   # random > in-built module
print(random.randint(1, 25))    # to generate random numbers between '1 and 25'
print(random.random())
print(random.randrange(ord('a'), ord('f')))
print(ord('a'))
print(ord('f'))
print(random.randrange(97, 102))
print(random.randrange(ord(input('Enter FA: ')), ord(input('Enter SA: '))))
a=5; b=9
print(random.randrange(a, b))
# c='y'; d='m'
# if c < d: 
#     print(random.randrange(ord(c), ord(d)))
# else:
#     print('pass')
