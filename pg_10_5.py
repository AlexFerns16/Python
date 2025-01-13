# supersets and subsets

s = {12, 15, 13, 23, 22, 16, 17}
t = {13, 15, 22}

# a set is said to be a 'subset' of a 'superset'
# only if all the elements of a 'subset' are included in a given 'superset'

print(s.issuperset(t))    # checks if 's' is a superset of 't'
print(s.issubset(t))      # checks if 's' is a subset of 't'          
print(s.isdisjoint(t))    # checks if the two sets are disjoint

a = {1, 2, 3, 4, 5}
b = {2, 4, 5}

# 'a' is a superset of 'b' hence 'a >= b' is 'True' 

# only if 'a' contains all the values of 'b'
# 'a' is said to be greater than 'b'
# i.e. 'a' is a superset of 'b'
print(a >= b)             
print(a <= b)

c = {1, 2, 3, 4, 5}
d = {5, 6, 7, 8}
print(c>d)
