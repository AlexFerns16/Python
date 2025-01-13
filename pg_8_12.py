print()
# -----------------------------------------------
lst_1 = [10, 20, 30]
lst_2 = [40, 50, 60]

lst_3 = []
for i in range(len(lst_1)):
    lst_3 = lst_3 + [lst_1[i] + lst_2[i]]
print(lst_3)
