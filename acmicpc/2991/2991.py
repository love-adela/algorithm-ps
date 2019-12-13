# boj.kr/2991
A, B, C, D = map(int, input().split())
lst = list(map(int, input().split()))
for i in lst:
    print(bool(0<i%(A+B)<=A)+bool(0<i%(C+D)<=C))
