count = 0
while count < 3:
    p = int(input('Enter the pricipal amount: '))
    n = int(input('Enter the number of years: '))
    r = float(input('Enter the rate of interest: '))

    si = (p * n * r) / 100
    print('pa = Rs. {}, noy = {}, roi = {}'.format(p, n, r))
    print('Simple Interest = Rs. {}'.format(si))

    count = count + 1
