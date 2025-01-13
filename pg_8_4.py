print()
# list concatenation --------------------------------

lst = [12, 15, 13, 23, 22, 16, 17]
lst = lst + [3, 44, 55]
print(lst)

print()
# list merging --------------------------------------

s = [10, 20, 30]
t = [100, 200, 300]
z = s + t
print(z)

print()
# converting to list using typecasting --------------
 
u = list('Africa')
print(u)
v = list((10, 20, 30))
print(v)
w = list({40, 50, 60})
print(w)
x = list({10:40, 20:50, 30:60}.keys())
print(x)
x = list({10:40, 20:50, 30:60}.values())
print(x)
x = list({10:40, 20:50, 30:60}.items())
print(x)

print()
# aliasing or shallow copy ----------------------------------

lst1 = [10, 20, 30, 40, 50]
lst2 = lst1
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))
lst1[0] = 100
print(lst1)
print(lst2)

print()
# cloning or deep copy ----------------------------------

lst1 = [10, 20, 30, 40, 50]
lst2 = [10, 20, 30, 40, 50]
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))

lst1[1] = 100
print(lst1)
print(lst2)

print()
lst3 = [10, 20, 30]
lst4 = [] + [10, 20, 30]
print(lst3)
print(lst4)
print(id(lst3))
print(id(lst4))

lst3[1] = 100
print(lst3)
print(lst4)

# print()
# x = 3
# y = x
# print(x)
# print(y)
# print(id(x))
# print(id(y))

# print()
# x = 4
# y = x
# print(x)
# print(y)
# print(id(x))
# print(id(y))

# print()
# x = 3
# y = 3
# print(id(x))
# print(id(y))

print()
# searching --------------------------------------

lst = ['a', 'e', 'i', 'o', 'u']

res = 'a' in lst
print(res)

res = 'a' not in lst
print(res)

print()
# identity ----------------------------------------

lst1 = [10, 20, 30, 40, 50]
lst2 = [10, 20, 30, 40, 50]
lst3 = lst1
print(lst1 is lst2)
print(lst1 is lst3)
print(lst1 is not lst2)

print()

num1 = 10
num2 = 10
s1 = 'Hi'
s2 = 'Hi'
print(num1 is num2)
print(s1 is s2)

print()
# comparison -----------------------------------

a = [1, 2, 5, 4]
b = [1, 2, 5]
print(a<b)

print()
# emptiness ------------------------------------

lst = [1, 2, 3]
if lst:
    print('Full List')

lst = []
if not lst:
    print('Empty List')

lst = []
print(bool(lst))

# Note that the following values are considered to be False
# None
# Number equivalent to Zero: 0, 0.0, 0j
# Empty string, list, and tuple: '', "", [], ()
# Empty set and dictionary: {}
