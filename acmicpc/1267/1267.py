n = int(input())
prices = list(map(int, input().split()))
y = m = 0
for price in prices:
    y += (price // 30 + 1) * 10
    m += (price // 60 + 1) * 15

if m == y:
    print('Y M', m)
elif m < y:
    print('M', m)
else:
    print('Y', y)




