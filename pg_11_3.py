# looping in dictionaries

courses = {'DAA':'CS', 'AOA':'ME', 'SVY':'CE'}

print()

# iterate over key:value pair
for i in courses.items():
    print(i)

print()

# iterate over keys
for i in courses.keys():
    print(i)

print()

for i in courses:
    print(i)

print()

# iterate over values
for i in courses.values():
    print(i)

# enumerate
courses = {'DAA':'CS', 'AOA':'ME', 'SVY':'CE'}

for ind, (key, val) in enumerate(courses.items()):
    print(ind, key, val)
