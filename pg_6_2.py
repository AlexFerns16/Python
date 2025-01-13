print()
# example 1 ----------------------------------

count = 0
while count < 5:
    print(count)
    count = count + 1

print()
# example 2 ----------------------------------

count = 0
while count < 5:
    print(count)
    count = count + 1
else:                       
    print(count)

# 'else' block goes to work
# when while condition becomes 'False'
# not stopping the execution of while loop abruptly

print()
# example 3 ----------------------------------

count = 0
while count < 5:
    if count == 3:
        break               # breaks the while loop abruptly stopping the excution of while loop
    print(count)
    count = count + 1
else:
    print(count)

print()
# example 4 ----------------------------------

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
else:
    print(count)
