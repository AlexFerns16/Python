# decision control instruction

# logical operators ------------------------
a = 40
b = 30

x = a==40
print(x)

y = b==30
print(y)

z = (a==40) and (b==30)     # 1 and 1 is 1
print(z)

z = (a==40) and (b==40)     # 1 and 0 is 0
print(z)

z = (a==50) and (b==30)     # 0 and 1 is 0
print(z)

z = (a==50) and (b==40)     # 0 and 0 is 0
print(z)

u = (a==50) or (b==40)      # 0 or 0 is 0
print(u)

u = (a==40) or (b==40)      # 1 or 0 is 1
print(u)

u = (a==50) or (b==30)      # 0 or 1 is 1
print(u)

u = (a==40) or (b==30)      # 1 or 1 is 1
print(u)
