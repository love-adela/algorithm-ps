t = int(input())
for _ in range(t):
    num, unit = input().split()
    if unit == 'kg':
        print('%.4f %s' % (float(num)*2.2046, 'lb'))
    elif unit == 'lb':
        print('%.4f %s' % (float(num)*0.4536, 'kg'))
    elif unit == 'l':
        print('%.4f %s' % (float(num)*0.2642, 'g'))
    elif unit == 'g':
        print('%.4f %s' % (float(num)*3.7854, 'l'))
