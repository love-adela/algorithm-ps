"""
가로길이 : M(1 ≤ M ≤ 50)
세로길이 : N(1 ≤ N ≤ 50)
배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
"""
import sys
sys.setrecursionlimit(10**8)
def dfs(curr_x, curr_y, visited):
    visited[curr_x][curr_y]= True; cnt = 1
    for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
        new_x = curr_x + dx
        new_y = curr_y + dy
        if 0<=new_x<N and 0<=new_y<M and not visited[new_x][new_y] and table[new_x][new_y] == 1:
            res = dfs(new_x, new_y, visited)
            cnt += res
    return cnt
    

T = int(input())
while T:
    M, N, K = map(int, input().split())
    table = [[0]* M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    count = 0
    for _ in range(K):
        (X, Y) = map(int, input().split())
        table[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if table[i][j] == 1 and not visited[i][j]:
                dfs(i,j, visited)
                count += 1
    print(count)
    T -= 1
