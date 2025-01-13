# example 1 -----------------------------------------------

s='Mumbai'
lst=['desert', 'dessert', 'to', 'too', 'lose', 'loose']
tpl=(10, 20, 30, 40, 50, 60)
i=0

while i < len(s):
    print(i, s[i], lst[i], tpl[i])
    i=i+1

# example 2 -----------------------------------------------

lst = ['dessert', 'desert', 'to', 'too', 'lose', 'loose']

i=0
while i<len(lst):
    s=lst[i]
    i=i+1
    j=0
    while j<len(s):
        print(s[j], end='\n')
        j=j+1
    print(end='\n')
