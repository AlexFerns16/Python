# looping in lists

animals = ['Zebra', 'Tiger', 'Lion', 'Jackal', 'Kangaroo']

i=0
while i < len(animals):
    print(animals[i])
    i=i+1

print()

for j in animals:
    for k in j:
        print(k)
    print()

print()

animals = ['Zebra', 'Tiger', 'Lion', 'Jackal', 'Kangaroo']

j=0
while j < len(animals):
    var = animals[j]
    j=j+1
    
    k=0
    while k < len(var):
        print(var[k])
        k=k+1
    print()

print()
# -------------------------------------------------

animals = ['Zebra', 'Tiger', 'Lion', 'Jackal', 'Kangaroo']

for index, a in enumerate(animals):
    print(index, a)
 