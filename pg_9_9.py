# sorting a 'list of tuples'
# or 'tuple of lists'

import operator

lst = [('abc', 24, 1.27), ('def', 25, 1.24)]
tpl = (['abc', 24, 1.27], ['def', 25, 1.24])

print()
print(sorted(lst))
print(sorted(tpl))

print()
print(sorted(lst, key=operator.itemgetter(2)))
print(sorted(lst, key=operator.itemgetter(2)))
