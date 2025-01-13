# --------------------------------------------------------------------------------------
# f.seek(0)               # beginning of the file
# f.seek(12, 0)           # 12 positions right from the beginning of the file
# f.seek(0, 2)            # end of the file
# f.seek(-10, 2)          # 10 positions left from the beginning of the file
# f.seek(5, 1)            # five positions right from the current position

# --------------------------------------------------------------------------------------
f = open('file_one', 'w+')
f.write('This is Python ver 3.7\n')
f.write('This is a programming language\n')
f = open('file_one', 'r')
f.seek(5)
a = f.read()
f.close()
print(a)
