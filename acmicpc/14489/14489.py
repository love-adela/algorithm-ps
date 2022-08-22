a, b = map(int, input().split()) # 잔고 A, B
c  = int(input()) # 치킨 가격

if (a + b) < c*2:
    print(a+b)
else:
    print(a+b -c*2)

