# lambda functions --------------------
# x = (lambda n : n * n * n)(5)
# print(x)

# x = lambda n : n * n * n
# y = x(7)
# print(y)

# regular function --------------------
# def func_prod(n):
#     p = n*n*n
#     return p

# x = func_prod(3)
# print(x)

# -------------------------------------
# s = (lambda stg : int(stg) + int(stg))(input('Enter a Number: '))
# print(s)

# -------------------------------------
# t = (lambda a, b, c : (a*b*c)/(a+b+c))(10, 20, 30)
# print(t)

# -------------------------------------
# u = (lambda stg : int(stg) + int(stg))(' 5 ')
# print(u)

# u = (lambda stg : int(stg.strip()) + int(stg.strip()))(' 5 ')
# print(u)

# -------------------------------------
# t = (lambda stg : stg.upper())(' python ')
# print(t)

# t = (lambda stg : stg.upper().strip())(' python ')
# print(t)

# -------------------------------------
# lst_one = [10, 20, 30]
# x = (lambda l : sum(l)/len(l))(lst_one)
# print(x)

# -------------------------------------
lst_two = [15, 25, 35]
x = (lambda l : [(i+i, i*i) for i in l])(lst_two)
print(x)

lst_two = [15, 25, 35]
x = (lambda l : [{i+i : i*i} for i in l])(lst_two)
print(x)

lst_two = [15, 25, 35]
x = (lambda l : {i+i : i*i for i in l})(lst_two)
print(x)

# example 1 -------------------------------------
# def arith(num):
#     x = (lambda a : a + 5)(num)
#     y = (lambda a : a - 5)(num)
#     z = (lambda a : a * 5)(num)

#     return x, y, z

# var_one = arith(5)
# print(var_one)

# var_two = arith(int(input('Enter Num: ')))
# print(var_two)

# example 2 -------------------------------------
x = (lambda x : ((lambda y : y + 5)(x) + 5))(5)
print(x)

# example 3 -------------------------------------
def funx(n):
    x = n*n*n
    return x

y = (lambda u : funx(u))(5)
print(y)
