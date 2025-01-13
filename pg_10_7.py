# updating set operations

a = {1, 2, 3, 4, 5}
b = {2, 4, 5}

a |= b      # a = a | b     # update 'a' with the result of 'a|b'
print(a)

a &= b      # a = a & b     # update 'a' with the result of 'a&b'
print(a)

a -= b      # a = a - b     # update 'a' with the result of 'a-b'
print(a)

# prints only the unique values 
# i.e. values which are not common between both the sets
a ^= b      # a = a ^ b     # update 'a' with the result of 'a^b'
print(a)
