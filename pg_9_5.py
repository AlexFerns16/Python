# try the following operations on tuple that were done on lists

# concatenation
# merging
# conversion
# aliasing
# cloning
# searching
# identity
# comparision
# emptiness

l1 = [10, 20, 30]
l2 = [] + l1
print(id(l1))
print(id(l2))

# does not creates a new object for 't2' in a tuple 
# because a tuple is immutable 
t1 = (10, 20, 30)
t2 = tuple() + t1         
print(id(t1))
print(id(t2))

# searching
print(10 in (20, 10, 5))

# identity
print((10, 20, 30) is (10, 20, 30))
print((10, 20, 30) is (20, 10, 30))
