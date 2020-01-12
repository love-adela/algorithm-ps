import sys
n, m = map(int, sys.stdin.readline().split())

    
def get_two(n, m):
    # n!에 있는 2의 개수
    k = n-m
    count_2 = 0
    while n > 0:
        n //= 2 
        count_2 += n
    
    # m!에 있는 2의 개수
    while m > 0:
        m //= 2
        count_2 -= m

    # (n-m)!에 있는 2의 개수
    while k > 0:
        k //= 2
        count_2 -= k
    return count_2

def get_five(n, m):
    # n!에 있는 5의 개수
    k = n-m
    count_5 = 0
    while n > 0:
        n //= 5
        count_5 += n

    # m!에 있는 5의 개수
    while m > 0:
        m //=5
        count_5 -= m

    # (n-m)!에 있는 5의 개수
    while k > 0:
        k //=5
        count_5 -= k

    return count_5

if n == 0 and m == 0:
    print(0)
else:
    print(min(get_two(n, m), get_five(n, m)))
