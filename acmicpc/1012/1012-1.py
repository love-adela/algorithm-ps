"""
배추밭의 가로길이:  M(1 ≤ M ≤ 50)
세로길이 : N(1 ≤ N ≤ 50)
배추가 심어져 있는 위치의 개수 :K
"""
import sys
sys.setrecursionlimit(10**8)
def dfs(curr_x, curr_y, visited):
    visited[curr_x][curr_y] = True; cnt = 1
    for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
        next_x = curr_x + dx
        next_y = curr_y + dy
        if 0<= next_x<M and 0<=next_y< N and not visited[next_x][next_y]:
            if table[next_x][next_y] == 1:
                res = dfs(next_x, next_y, visited)
                cnt += res
    return cnt


T = int(input())
while T:
    M, N, K = map(int, input().split())
    table = [[0] * N for _ in range(M)]
    visited = [[False]*N for _ in range(M)]
    answer = 0
    for _ in range(K):
        Y, X = map(int, input().split())
        table[Y][X] = 1
    for i in range(M):
        for j in range(N):
            if table[i][j] == 1 and not visited[i][j]:
                dfs(i, j, visited)
                answer += 1
    print(answer)
    T -= 1
