import math

print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.fabs(-3))
print(math.factorial(5))
print(math.log(5))
print(math.log10(5))
print(math.exp(3))
print(math.trunc(5.26589))
print(math.ceil(5.2))
print(math.floor(5.2))
print(math.modf(5.2537))

# degrees(x)
# radians(x)
# sin(x)
# cos(x)
# tan(x)
# sinh(x)
# cosh(x)
# tanh(x)
# acos(x)
# asin(x)
# atan(x)
# hypot(x, y)


print()
# example ----------------------------------------------

#1.
print(round(math.pi, 2))
print(round(math.e, 2))
print(int(math.sqrt(9)))
print(math.ceil(-5.2))
print(math.floor(-5.2))

#2.
x = math.modf(5.2537)
print(x)
x_1 = x[0]
x_2 = x[1]
print(x_1)
print(x_2)
u = round(x_1, 2)
print(u)
v = int(u * 100)
print(v)
