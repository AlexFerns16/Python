lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']
s = 'Mumbai'
i = 0

for i in range(len(lst)):
    if i > 2:
        break
    else:
        print(i, lst[i], s[i])

print()
# --------------------------------------

for i in range(len(lst)):
    if i < 3:
        print(i, lst[i], s[i])
    else:
        break
