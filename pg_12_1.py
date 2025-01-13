# list comprehensions

a = [(x, x**2, x**3) for x in range(1, 4)]
print(a)

b = [x for x in range(1, 4)]
print(b)

c = [int(x) for x in ['10', '20', '30', '40']]
print(c)
