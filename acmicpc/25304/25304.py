x = int(input()) # 영수증에 적힌 금액 x
n = int(input()) # 물건의 종류의 수 n

total = 0
for _ in range(n):
    a,b = map(int, input().split()) # a: 물건가격 b: 물건개수
    total += a*b
if total == x:
    print('Yes')
else:
    print('No')

