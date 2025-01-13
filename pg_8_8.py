# list varieties

print()
# nested lists ----------------------------
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
c = [a, b]
print(c)
print(c[0][2], c[0][0], c[1][2])

print()
# embedded lists ----------------------------
x = [1, 2, 3, 4]
y = [10, 20, x, 30]
print(y)
print(y[2][2])

print()
# unpack a string or list, within a list, using the * operator
s = 'Hello'
l = [*s]
print(s)
print(l)

x = [1, 2, 3, 4]
y = [10, 20, *x, 30]
print(y)

# examples -------------------------------

c = [[0, 1, [2, 3], 4], 5, [6, 7]]
print(c[0][2][1])
