# ------------------------------------
msg = 'Give your career a competitive edge with globally recognized certifications\n\n'
msgs = ['Python\n', 'SQL\n', 'HTML\n', 'CSS\n', 'Bootstrap\n', 'JavaScript\n']

f = open('doc_two', 'w')
f.write(msg)
f.writelines(msgs)
f.close()

f = open('doc_two', 'r')
data = f.read()
print(data)
f.close()
