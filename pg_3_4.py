# arithmatic operators

print(5+2)                  # addition
print(5-2)                  # subtraction
print(5/2)                  # division
print(5//2)                 # division > quotient discarding the fractional part
print(5%2)                  # remainder
print(5.5%2)
print(5*2)                  # multiplication
print(5**2)                 # exponential


a=10
b=20
c=30

a = a+10
a += 10
print(a)

# example ----------------------------

print(2**2**4)              # right to left

print(2**3 + 3**2)          # left (2**2) to right (3**2) due to '+' operator

print(2**3**4 + 2**2**4)    
# left (2**3**4) > right to left (2**81)
# to
# right (2**2**4) > right to left (2**16)

num = 12345
for i in range(5):
    rem = num % 10
    print(rem)
    num = num // 10
