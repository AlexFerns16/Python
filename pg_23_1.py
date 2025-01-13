# ---------------------------------
msg_one = 'This is line 1\n'
msg_two = 'This is line 4\n'

f = open('messages', 'w+')
f.write(msg_one)
f.write(msg_two)
f.close()

f = open('messages','r')
data = f.read()
print(data)
f.close()
