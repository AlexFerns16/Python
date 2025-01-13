# -----------------------------------
x = '153'
lenx = len(x)
sum = 0

def fun(j):
    return int(j)

for i in x:
    y = fun(i)
    sum += y**lenx

print(sum)
