# tuple methods

tpl = (12, 15, 13, 23, 22, 45, 74, 22)

print(tpl.count(23))    # returns no. of times 23 appears in tpl
print(tpl.index(22))    # returns index of item 22


# example --------------------------------------------
for index, a in enumerate(tpl):
    if a==22:
        print(index, a)
