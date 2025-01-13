# categories of string methods

stg_1 = 'Hello'
stg_2 = '12345'
stg_3 = 'He123'
stg_l = 'python'
stg_u = 'PYTHON'
string_w_1 = '    Hello   '
string_w_2 = ' Hello '
stg_4 = 'i love python'
stg_5 = ' i love python'
s = '_'

print()
# isalpha() > checks if all characters in string are alphabets

print(stg_1.isalpha()) 
print(stg_2.isalpha())
print(stg_3.isalpha())

print()
# isdigit() > checks if all characters in string are digits

print(stg_1.isdigit())
print(stg_2.isdigit())
print(stg_3.isdigit())

print()
# isalnum() > checks if all characters in the string are alphabets or digits

print(stg_1.isalnum())
print(stg_2.isalnum())
print(stg_3.isalnum())

print()
# islower() > checks if all characters in string are lowercase alphabets

print(stg_1.islower())
print(stg_l.islower())
print(stg_u.islower())

print()
# isupper() > checks if all characters in string are uppercase alphabets

print(stg_1.isupper())
print(stg_l.isupper())
print(stg_u.isupper())

print()
# startswith() > checks if string starts with a value

print(stg_1.startswith('H'))
print(stg_1.startswith('h'))
print(stg_1.startswith('He'))
print(stg_1.startswith('Ho'))

print()
# endswith() > checks if string ends with a value

print(stg_1.endswith('o'))
print(stg_1.endswith('e'))
print(stg_1.endswith('lo'))
print(stg_1.endswith('Lo'))

print()
# find() > searches a value and returns its position

print(stg_1.find('l'))

print()
# replace() > replace one value with another

print(stg_1.replace('l', 'L'))
x = stg_1.replace('H', 'h')         # does not change the original value in stg_1
print(x)
print(stg_1)

print()
# lstrip() > removes whitespaces from the left of the string including tab
# rstrip() > removes whitespaces from the right of the string including tab
# strip() > removes whitespaces from left and right including tab

print(string_w_1)
print(string_w_2)
print(string_w_1.lstrip())
print(string_w_2.lstrip())
print(string_w_1.rstrip())
print(string_w_2.rstrip())
print(string_w_1.strip())
print(string_w_2.strip())

print()
# split() > split the string at a specified seperator string

print(stg_4.split(' '))
print(stg_4.split())        # by default > .split() is taken as .split(' ')
# print(stg_l.split(''))    # .split('') > empty seperator not allowed

print()
# s.join(stg) > joins string 's' to each element of string 'stg' except the last element

print(s.join(stg_u))
print(stg_u)
y = s.join(stg_u)
print(y)
print(y.split('_'))

print()
# partition() > partitions string into three parts at first occurence of specified string

print(stg_4.partition('love'))
print(stg_4.partition('lo'))
print(stg_4.partition(' '))
print(stg_5.partition(' '))


# examples -------------------------------------------------

for p, i in enumerate(stg_1):
    if 'l' in i:
        print(p, i)
