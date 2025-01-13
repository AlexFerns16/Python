i=1
while i<=3:
  j=1
  while j<=3:
    k=1
    while k<=3:
      if i==j or j==k or k==i:
        k+=1
        continue
      else:
        print('R:', i, j,  k)
      k+=1
    j+=1
  i+=1

print()
# -----------------------------------
print()

i=1
print('i=1')
while i<=3:
  j=1
  print('j=1')
  while j<=3:
    k=1
    print('k=1')
    while k<=3:
      if i==j or j==k or k==i:
        print('T:', i, j, k)
        k+=1
        continue
      else:
        print('R:', i, j,  k)
      k+=1
      print('k')
    j+=1
    print('j')
  i+=1
  print('i')
