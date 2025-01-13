def print_it(**kwargs):
    print(kwargs)
    print(kwargs.items())
    print(kwargs.values())
    print(kwargs.keys())
    print(*kwargs.items())

# print_it(a=10)
print_it(a=10, b=20, c=30)


 
print()
#----------------------------------------------
dct = {'Student':'Ajay', 'Age':23}
print_it(**dct)



print()
#----------------------------------------------
dct_x = {'student':'anil', 'age':25}
# dct_up = **dct_x                          # error

# **dct_x   >   'student'='anil', 'age'=25
# 'student'='anil', 'age'=25    >    only serves as arguments to a function


# example 1 
def func1(student, age):
    print(student + ' is the name of the student')
    print(str(age) + ' is the age of the student')

func1(**dct_x)       # func(student='anil', age=25)


# example 2 
def func2(student='amol', age=20):
    print(student + ' is the name of the student')
    print(str(age) + ' is the age of the student')

func2(**dct_x)       # func(student='anil', age=25)
func2()
func2(age=40)
func2(student='raj')
func2(dct_x)


# example 3 
def func3(student='amol', age=20):
    print(student)
    print(age)

func3(dct_x)
