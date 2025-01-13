# set methods

s = {12, 15, 13, 23, 22, 16, 17}
t = {'A', 'B', 'C'}
u = set()
tpl = (10, 20, 30)

s.add('Hello')      # concatenation
print(s)

s.update(t)         # merging
print(s)

s.update((tpl,))
print(s)

u = s.copy()        # cloning
print(u)

s.remove(15)
print(s)

# s.remove(101)     # error, 101 is not a member of set
# print(s)

s.pop()             # removes the first element from the accessing order of the given set
print(s)

s.pop()
print(s)

s.discard(17)
print(s)

s.discard(101)      # doesn't raises an error even when '101' is not a member of set
print(s)

s.clear()           # clears all elements
print(s)    
