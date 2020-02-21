N, M = map(int, input().split())
balls = [int(param)+1 for param in range(N)]
for i in range(M):
    i, j = map(int, input().split())
    balls[i-1], balls[j-1] = balls[j-1], balls[i-1]
print(' '.join(map(str, balls)))
