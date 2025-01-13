# set varieties -----------------------------------------------

# a set cannot contain a set embedded in it
# nested sets are not permitted
# s = {'gate', 'fate', {10, 20, 30}, 'late'}

# unpacking a set
x = {1, 2, 3, 4}
print(*x)

x = {1, 2, 3, 4}
y = [*x]
print(y)
