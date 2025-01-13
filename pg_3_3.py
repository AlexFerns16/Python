# multiple variable assignment

a=10
b=20
c=a+b
print(c)

a=30; b=40; c=a+b
print(c)

c, d, e = 10, 20, 30
f=c+d+e
print(f)

g = h = i = 5
print(g + h + i)


# example ------------------------------

u = 5; v = 6
print(u, v)

u, v = v, u
print(u, v)

print()                 # newline space

j = 15 
k = 25 
temp=0
print(j, k)

temp = j
j = k
k = temp
print(j, k)

# does not work -----------------------

# x, y, z = 30, 40, 30+y
# o=x+y+z
# print(o)

# x, y, z = 30, 40, x+y
# o=x+y+z
# print(o)
