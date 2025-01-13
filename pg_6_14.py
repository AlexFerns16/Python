# armstrong number
# 153 < (1)^3 +(5)^3 + (3)^3 = 1 + 125 + 27 = 153

# num = 153

# r1 = num % 10           # r1 = 3
# print(r1)

# d1 = num // 10          # d1 = 15
# print(d1)

# r2 = d1 % 10            # r2 = 5
# print(r2)

# q1 = d1 // 10           # q1 = 1
# print(q1)

# print((r1)**3 + (r2)**3 + (q1)**3)

# -----------------------------------------------------------------------------------------
# method 1 ------------------------------------------
num = input('Enter the Number: ')       # entered number in string
i_num = int(num)                        # entered number in integer
sum = 0

l = len(num)                            # length of the number
print(l)

temp = i_num                            # storing the integer number in temporary register
print(temp)

i = 0
while i < l:
    digit = temp % 10                   # remainder
    sum = sum + (digit) ** l            # (digits) exp (length)
    temp = temp // 10                   # quotient
    i += 1

print(sum)

# method 2 ------------------------------------------
number = '9474'
sum=0
for i in number:
    sum = sum + (int(i)**len(number))
print(sum)
