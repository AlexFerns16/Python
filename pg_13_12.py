print()
# --------------------------------------------------------
def cal_sum_prod(x, y, z):
    ss = x + y + z
    pp = x * y * z
    return ss, pp

s, p = cal_sum_prod(10, 20, 30)         # returns 'ss' to 's' and 'pp' to 'p'
print(s, p)

sp = cal_sum_prod(10, 20, 30)           # returns a tuple of '(ss, pp)' to 'sp'
print(sp)
