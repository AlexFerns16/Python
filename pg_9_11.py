# ------------------------------------------------

x = [10, 20, 30, 40, 50]
y = ['P', 'y', 't', 'h', 'o', 'n']
s = 'Python'

a = 0
for i in x:
    a = a + i
print(a)

a = []
for i in x:
    a = a + [i+5]
print(a)

b = ''
for i in y:
    b = b + i
print(b)

b = []
for i in s:
    b = b + [i]
print(b)
