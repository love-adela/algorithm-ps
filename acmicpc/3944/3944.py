import sys
read = sys.stdin.readline
T = int(input())
for _ in range(T):
    B, D = read().split() 
    B = int(B)
    num = 0
    for i in D: 
        num += int(i, B) % (B-1)
    print(num % (B-1))
