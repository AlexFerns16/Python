print()
# ------------------------------------------------
def func(students):
    print(students)

dct_1 = {'name':'abc', 'age':25}
func(students=dct_1)


print()
# ------------------------------------------------
def func(**students):
    print(students)

dct_1 = {'name':'abc', 'age':25}
dct_2 = {'name':'def', 'age':27}

func(_1=dct_1, _2=dct_2)
