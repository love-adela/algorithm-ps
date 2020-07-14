def snail(C, R):
    grid = [[0]* C for _ in range(R)]
    count, offset = 0, 0
    max_size = C*R
    while R > 0 and C > 0:
        for i in range(offset+R-1, offset-1, -1):
            if count >= max_size:
                break
            count += 1
            grid[i][offset] = count
        for j in range(offset+1, offset+C):
            if count >= max_size:
                break
            count += 1
            grid[offset][j] = count
        for i in range(offset+1, offset+R):
            if count >= max_size:
                break
            count += 1
            grid[i][offset+C-1] = count
        for j in range(offset+C-2, offset, -1):
            if count >= max_size:
                break
            count += 1
            grid[offset+R-1][j] = count

        offset +=1 
        R -=2 
        C -=2 
    return grid

C, R = map(int, input().split())
K = int(input())
table = snail(C, R)

def main():
    if C*R < K: 
        return 0
    for i in range(R):
        for j in range(C):
            if table[i][j] == K:
                return ' '.join(list(map(str, [j+1, R-i])))
print(main())
