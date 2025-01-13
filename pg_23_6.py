# serialization / deserialization of a list ----------

import json

f = open('file_two', 'w+')
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
json.dump(lst, f)
f.seek(0)
inlst = json.load(f)
print(list(inlst + [100]))
f.close()

# serialization / deserialization of a tuple ----------

import json

f = open('file_two', 'w+')
tpl = ('Python', '3+2j', True)
json.dump(tpl, f)
f.seek(0)
intpl = json.load(f)
print(tuple(intpl) + (110,))
f.close()

# serialization / deserialization of a dictionary ----------

import json

f = open('file_two', 'w+')
dct = {'Anil':24, 'Ajay':23, 'Nisha':22}
json.dump(dct, f)
f.seek(0)
indct = json.load(f)
print({**dict(indct), **{'Krutika':18}})
f.close()
