# what are dictionaries ---------------------------------

# empty dictionary
d1 = {}

# key:value pair
d2 = {'A101':'Amol', 'A102':'Anil', 'B103':'Ravi'}

# different keys may have same values
d3 = {10:'A', 20:'A', 30:'Z'}       

# if two keys are same then, the latest key:value pair gets stored
d4 = {10:'A', 20:'B', 10:'Z'}
print(d4)

# if key:value pairs are repeated, then only one pair gets stored
d5 = {10:'A', 20:'B', 10:'A'}
print(d5)
