print(abs(-3))
print(abs(-3.3))
print(pow(5, 2))
print(pow(5, -2))
print(min(5, 2, 3, 7))
print(max(5, 2, 3, 7))
print(divmod(5, 2))
print(round(3.2547896458, 2))
print(bin(65))
print(oct(65))
print(hex(65))

# example ---------------------------------------------

# 1.
# x = divmod(5, 2)
# print(x[0])
# print(x[1])

# 2.
# print(max(5, 2, 3, 7+2))

# 3.
# print(max(5, 2, 3, 7+2, int(input('Enter Num: '))))

# 4.
# print(max(5, 3, 2+int(input('Enter Num: ')), 9))

#5.
# print(round(pow(5.256848, 2), 2))

#6.
# print(round(pow(7.5895, 2), 2))

#7.
# print(min(2.56, 3.56, 8.98))
# print(min('a', 'b', 'c'))

#8. 
# print(min('a', 'b', 'c', chr(96)))
# 'a'>97, 'b'>98, 'c'>99, '`'>96

#9.
# print(min('a', 'b', 'c', str(96)))
# 'a'>97, 'b'>98, 'c'>99, '96'>5754(only the decimal value of first character '9' i.e. 57 is compared)

#10.
# print(min(round(pow(5.256848, 2), 2), round(pow(7.5895, 2), 2), 8.98))
# print(min(round(pow(5.256848, 2), 2), round(pow(7.5895, 2), 2), round(pow(9.4595, 2), 2)))
