# example 1 -------------------------------------------------------

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

y=[]; i=0
for row in range(3):
    x=[]
    for col in range(3):
        x=x+[lst[i]]
        i+=1
    y=y+[x]
print(y)

# example 2 -------------------------------------------------------

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

y=[]; i=0
for row in range(5):
    x=[]
    for col in range(3):
        if i<len(lst):
            x=x+[lst[i]]
            i+=1
        else:
            x=x+[]
    y=y+[x]
print(y)

# example 3 -------------------------------------------------------

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

# y=[]; i=0
# for row in range(8):
#     x=[]
#     for col in range(2):
#         if i<len(lst):
#             x=x+[lst[i]]
#             i+=1
#         else:
#             x=x+[0]
#     y=y+[x]
# print(y)

# example 4 -------------------------------------------------------

# import math

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
# gvn_col = int(input('Enter the number of columns: '))

# len_list = len(lst)
# exp_row = math.ceil(len_list/gvn_col)

# y=[]; i=0
# for row in range(exp_row):
#     x=[]
#     for col in range(gvn_col):
#         if i<len(lst):
#             x=x+[lst[i]]
#             i+=1
#         else:
#             x=x+[0]
#     y=y+[x]
# print(y)
