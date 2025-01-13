# -------------------------------------
tpl = (10, 20, 30)
lst = [100, 200, 300]
st = {'a', 'b', 'c'}
dct = {1:'10', 2:'20', 3:'30'}

f = open('doc_three', 'w')
f.write(str(tpl)+'\n')
f.write(str(lst)+'\n')
f.write(str(st)+'\n')
f.write(str(dct)+'\n')
f.close()
