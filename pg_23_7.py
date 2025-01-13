# -------------------------------------
import json

lst = [10, 20, 30, 40, 50]
tpl = ('Python', '3+2j', True)
dct = {'Anil':25, 'Amol': 24}

str1 = json.dumps(lst)
str2 = json.dumps(tpl)
str3 = json.dumps(dct)

print(str1)
print(str2)
print(str3)

print()

l = json.loads(str1)
t = json.loads(str2)
d = json.loads(str3)

print(l)
print(t)
print(d)
