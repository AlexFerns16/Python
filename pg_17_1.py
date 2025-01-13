def func():
    a = 45

    global b
    b = 6.28
    print(id(b))

    print(a, b, s)

a = 20
b = 3.14
s = 'Python'

# print(id(b))
func()
# print(id(b))
# print(id(6.28))
print(a, b, s)
