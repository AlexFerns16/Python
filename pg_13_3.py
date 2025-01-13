# communication with functions
 
def cal_sum(x, y, z):
    return x+y+z

a = cal_sum(10, 20, 30)
print(a)

b = cal_sum(40, 50, 60)
print(b)

c = cal_sum (
    int(input('Enter x: ')), 
    int(input('Enter x: ')), 
    int(input('Enter x: '))
)
print(c)

a=10; b=20; c=30
z = cal_sum(a, b, c)
print(z)
