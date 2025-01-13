# serialization / deserialization of a nested dictionary ----------

import json

f = open('file_two', 'w+')
dct = {
    'Anil':{'DOB':'17/11/98', 'Fav':'Igloo'},
    'Amol':{'DOB':'18/12/95', 'Fav':'Tundra'},
    'Ravi':{'DOB':'12/8/93', 'Fav':'Artic'}
}
json.dump(dct, f)
f.seek(0)
indct = json.load(f)
print(dict(indct))
f.close()
