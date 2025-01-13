# recursion


# -----------------------------------------------------------
# def fun(num):
#     if num > 100:
#         return num - 10
#     return fun(fun(num + 11))

# print(fun(75))


# -----------------------------------------------------------
# def fun(num):
#     num -= 10
#     print(num)

#     if num > 50:
#         return fun(num)
    
#     return 50 * 100

# print(fun(100))


# -----------------------------------------------------------
# def fun1(num):
#     def fun2(num):
#         num -= 10
#         print(num)
#         if num > 50:
#             return fun1(num)
#         else:
#             return 1
#     fun2(num)
#     return 1

# print(fun1(100))
