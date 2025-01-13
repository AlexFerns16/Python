# what are lists?

num_one = [10, 20, 30, 40, 50]
print(num_one)
print(num_one[2])                   # accessing the elements of a list

print()                             # newline space

num_two = [10] * 5
print(num_two)
print(id(num_two))

print()                             # newline space

num_two = []
print(num_two)                      # assigns a new list to a variable
print(id(num_two))

print()                             # newline space

names = ['Sanjay', 'Anil', 'Radha']
x = ['Zebra', 10, 5.26, 3+2j]
print(names)
print(x)

print()                             # newline space

ages = [25, 26, 25, 27, 26]         # duplicates allowed in a list
num = [10] * 5                      # [10, 10, 10, 10, 10]
lst = []                            # empty list
print(ages)
print(num)
print(lst)

print()                             # newline space

# accessing lists elements / accessing elements in list

lst_one = ['I', 'am', 'here'] 
print(lst_one)
print(lst_one[1])                   # accessing through index position


var_one = lst_one[2]
print(var_one)
print(var_one + ' I' + ' am')       # string concatenation
print(lst_one[2] + ' I' + ' am')
print(lst_one[2] + ' ' + lst_one[0] + ' ' + lst_one[1])
print(lst_one[0] + ' ' + lst_one[1] + ' ' + 'everywhere')

print()                             # newline space

lst_two = [10, 20, 30, 40, 50]
print(str(lst_two[0]) + ' is a number')
print(lst_two[1], lst_two[3])

print()                             # newline space

# list slicing

lst_two = [10, 20, 30, 40, 50]
print(lst_two[1:4])
print(lst_two[1:5])

lst_tp_one = lst_two[2:4]
print(lst_tp_one)

lst_tp_two = lst_two[1] + lst_two[3]
print(lst_tp_two)

print(lst_two[:4])
print(lst_two[3:])
print(lst_two[:])

print()

animals = ['Zebra', 'Tiger', 'Lion', 'Jackal', 'Kangaroo']
print(animals[1:3])
