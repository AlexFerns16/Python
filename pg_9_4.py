# basic tuple operations
# ---------------------------------------------------

msg = ('Fall', 'in', 'love', 'with', 'Python')
# msg[4] = 'Java'                  # error > cannot mutate a tuple
# msg[1:3] = ('Above', 'Mark')     # error > cannot mutate a tuple

# mutable lists, and immutable string all can belong to tuple
s = ([1, 2, 3, 4], [4, 5], 'Python')
print(s)

# list inside a tuple is mutable -------------------------
s = ([1, 2, 3, 4], [4, 5], 'Python')
s[0][2] = 33
print(s)

t = s[1]            # copying the memory address of 's[1]' in 't'
print(t)
t[1] = 55           # mutates the original list 's[1]'
print(s)
