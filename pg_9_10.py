print()
# -------------------------------------
x = 10
print(x)

print()
# -------------------------------------
x = 10, 20
print(x)

print()
# -------------------------------------
x = (10, 20)
print(x)

print()
# -------------------------------------
x, y = 10, 20
print(x)
print(y)

print()
# -------------------------------------
x, y = (10, 20)
print(x)
print(y)

print()
# -------------------------------------
tpl = (10, 20, 30, 40, 50)

a, b, c, d, e = tpl
print(a, b, c, d, e)

x, _, _, _, y = tpl
print(x, y, _)

x, *_, y = tpl          # here '*' is used for variable-length
print(x, y, _)
print(x, y, *_)
