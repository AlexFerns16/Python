# ---------------------------------
f = open('doc_two', 'r')

# -----------------------------------
data_one = f.read()                    # reads the entire file and returns as string
print(data_one)

# -----------------------------------
data_two = f.read(20)                  # reads 'n' characters and returns a string
print(data_two)

# -----------------------------------
data_three = f.readline()              # reads a line and returns a string
print(data_three)

# -----------------------------------
while True:
    data_four = f.readline()
    if data_four == '':
        break
    print(data_four, end='')

# -----------------------------------
while True:
    data_four = f.readline()
    if data_four == 'CSS\n':
        print(data_four, end='')
        break
    print(data_four, end='')

# -----------------------------------
count = 1
while True:
    if count <= 4:
        data_four = f.readline()
        print(data_four, end='')
        count += 1
    else:
        break

# -----------------------------------
print(list(f))

for char in list(f):
    print(char, end='')

# -----------------------------------
for ind, char in enumerate(f):
    if ind >= 3 and ind <= 5:
        data_five = f.readline()
        print(data_five, end='')

# -----------------------------------
x = list(f)
print()

print(x)
for i in range(2, 4):
    print(x[i], end='')

# -----------------------------------
data_six = f.readlines()
print(data_six)

f.close()
