# type conversion
# typecasting

print(int(10.5))            # float to int
print(int('1'))             # string to int
print(int(True))            # boolean to int
print(int(False))           # boolean to int
print(int(b'\x31'))         # bytes (hex 30 to hex 39) to int

print()                     # newline space

print(float(10))            # integer to float
print(float('10.5'))        # float string to float
print(float('1'))           # integer string to float
print(float(b'\x31'))       # bytes (hex 30 to hex 39) to float
print(float(True))          # boolean to float
print(float(False))         # boolean to float

print()                     # newline space

print(str(1))               # integer to string
print(str(1.5))             # float to string
print(str(3+2j))            # complex to string
print(str(b'\x31'))         # bytes to string
print(str(True))            # boolean to string
print(str(False))           # boolean to string

print()                     # newline space

print(bool(1))              # integer to bool
print(bool(100))
print(bool(-100))
print(bool(0))
print(bool('Python'))       # ASCII char to bool
print(bool(''))
print(bool(' '))
print(bool(None))
print(bool(3+2j))           # complex to bool
print(bool(0+0j))            
print(bool(0+2j))
print(bool(3+0j))
print(bool(-3.57))
print(bool(int(b'\x30')))    # " b'\x30 " has a decimal value " 0 "
print(bool(int(b'\x31')))    # " b'\x31 " has a decimal value " 1 "

print()                      # newline space

print(complex(3))            # converting to complex
print(complex(3, 2))
print(complex(True, False))
print(complex(int(b'\x30')))
print(complex(int(b'\x37'), int(b'\x30')))

print()

print(type(10))

print()
#  examples --------------------------------

print(int('1') + int('2'))

print()
# ------------------------------------------

a=10
b=20
z=a+b
print('The output of a+b is: ' + str(z))

print()
# ------------------------------------------

print(str(int(True)))

# doesn't execute --------------------------

# print(int(3+2j))          # complex to int
# print(int('1.5'))         # float string to int
# print(float(3.5+4.2j))    # complex to float
