# boj.kr/2991
A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())
print((1 if P%(A+B)> 0 and P%(A+B) <= A else 0) + (1 if P%(C+D) > 0 and P%(C+D) <= C else 0))
print((1 if M%(A+B)> 0 and M%(A+B) <= A else 0) + (1 if M%(C+D) > 0 and M%(C+D) <= C else 0))
print((1 if N%(A+B)> 0 and N%(A+B) <= A else 0) + (1 if N%(C+D) > 0 and N%(C+D) <= C else 0))
