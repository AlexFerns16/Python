# --------------------------------------------------------------
def cal_sum(x=10, y=20):
    return x+y

print()
print(cal_sum())

print()
print(cal_sum(20, 40))
print(cal_sum(x=30, y=50))

print()
print(cal_sum(30))              # by default, assigned to the first argument in the function
print(cal_sum(y=30))

print(cal_sum(30+50, 7.5))

print(cal_sum([10, 20], [30, 40]))

# -------------------------------------------------------
def cal_mul(x, y=5, z=7):
    return x*y*z

print(cal_mul(1, 2))
# print(cal_mul(y=1, z=2))      # missing one required positional argument
print(cal_mul(2, z=2))
