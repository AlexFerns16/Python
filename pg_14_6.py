# higher order functions

print()
d = {'Oil':230, 'Clip':150, 'Stud':175, 'Nut':35}
print(d)

print()
d_1 = d.items()     # [('Oil', 230), ('Clip', 150), ('Stud', 175), ('Nut', 35)]
print(d_1)

print()
d_2 = sorted(d.items(), key=lambda kv:kv[1])
print(d_2)

print()
d_3 = sorted(d.items(), key=lambda kv:kv[0])
print(d_3)
