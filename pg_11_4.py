# basic dictionary operations

# creating a dictionary
courses = {
    'CS101':'CPP', 'CS102':'DS', 'CS201':'OOP',
    'CS226':'DAA', 'CS601':'Crypt', 'CS442':'Web'
}
print(courses)

# adding a key:value pair to dictionary
courses['CS444'] = 'Web Services'
print(courses)

courses[True] = 'Web Ser 1'
print(courses)

# updating the 'value' of the existing 'key:value' pair in a dictionary
courses['CS201'] = 'OOP Using Java'

# 'True' and '1' are considered the same
# 'False' and '0' are considered the same
print(courses[True])
print(courses[1])

# integer '1' is not added as a seperate 'key' to the dictionary
# updates 'True: Web Ser 1' to 'True: Web Ser 2'
courses[1] = 'Web Ser 2'
print(courses)

# copying the values of one item to another
courses['CS102'] = courses['CS601']
print(courses)

courses['CS102'] = courses['CS601'] = courses['CS442']
print(courses)

# writing the key as sum of two integers
courses[10+20] = 300
print(courses)

# delete a 'key:value' pair
# del(courses['CS102'])
print(courses)

# clearing the complete dictionary
# courses.clear()         # method 1
print(courses)

# courses = {}            # method 2
print(courses)

# deletes dictionary
# del(courses)
# print(courses)
