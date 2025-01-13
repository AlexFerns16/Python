for char in 'Leopard':
    print(char, end='')

print()

for animal in ['Cat', 'Dog', 'Tiger', 'Lion', 'Leopard']:
    print(animal)

print()

for i in ('Rose', 'Lily', 'Jasmine'):
    print(i)

print()

for num in {10, 20, 30, -10, -25}:
    print(num)

print()

for num in {-10, 20, -25, 10, 30, 10}:
    print(num)

print()

for key in {'A101':'Rajesh', 'A111':'Sunil', 'A112':'Rakesh'}:
    print(key)

print()

for key in {'A101':'Rajesh', 'A111':'Sunil', 'A112':'Rakesh'}.keys():
    print(key)

print()

for value in {'A101':'Rajesh', 'A111':'Sunil', 'A112':'Rakesh'}.values():
    print(value)

print()

for item in {'A101':'Rajesh', 'A111':'Sunil', 'A112':'Rakesh'}.items():
    print(item)

print()

for key, value in {'A101':'Rajesh', 'A111':'Sunil', 'A112':'Rakesh'}.items():
    print(key, value)
