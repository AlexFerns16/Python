# basic list operations

print()
# -----------------------------------------------------------------

animals = ['Zebra', 'Tiger', 'Lion', 'Jackal', 'Kangaroo']
ages = [25, 26, 25, 27, 26, 28, 25]
print(animals)
print(ages)

print()
animals[2] = 'Rhinoceros'
print(animals)
ages[5] = 31
print(ages)

print()
ages[2:5] = [10, 20, 30]
print(ages)
ages[1:3] = [40, 50, 60, 70]
print(ages)
ages[6:9] = [80, 90]
print(ages)
ages[2:5] = []
print(ages)
ages[:] = []                            # ages = []
print(ages)
