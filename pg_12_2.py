# comprehensions ---------------------------
def cal_sum(*args):
    return sum(args)

z = [int(input('Enter')) for i in range(3)]
result = cal_sum(*z)
print(result)
