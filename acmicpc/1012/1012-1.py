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
        # 무한루프가 돌지 않게 처리 : 옆에 있는 정점끼리 왔다갔다 하는걸 막음
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
            # 연결요소가 여러개이기 때문에 visited 체크를 해줘야 함
            # 다녀왔던 정점도 dfs가 가능하다고 여기지 않게 막음
            if table[i][j] == 1 and not visited[i][j]:
                dfs(i, j, visited)
                answer += 1
    print(answer)
    T -= 1
