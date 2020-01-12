import sys
n, m = map(int, sys.stdin.readline().split())

if n == 0 and m == 0:
    print(0)
else:
# n!에 있는 2의 개수
# 예를 들면 100!에 5가 몇 개인지 세려면
# 100/5=20, 20/5=4, 4/5=0 이렇게 해서 20+4를 하면 됨


    count_2 = 0
    while n > 0:
        n //= 2 
        count_2 += n
    print(count_2)
    
# n!에 있는 5의 개수
    count_5 = 0
    while n > 0:
        n //= 5
        count_5 += n
    print(count_5)

# m!에 있는 2의 개수
    while m > 0:
        m //= 2
        count_2 -= m
    print(count_2)

# m!에 있는 5의 개수
    while m > 0:
        m //=2
        count_5 -= m
    print(count_5)

# (n-m)!에 있는 2의 개수
    k = n-m
    while k > 0:
        k //= 2
        count_2 -= k
    print(count_2)
# (n-m)!에 있는 5의 개수
    while k > 0:
        k //= 2
        count_5 -= k
    print(count_5)


