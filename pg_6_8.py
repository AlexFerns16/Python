for ele in [10, 20, 30, 40, 50]:
    if ele % 10 != 0:
        print(ele, 'is not a multiple of 10')
        break
else:
    print('all numbers are multiple of 10')
