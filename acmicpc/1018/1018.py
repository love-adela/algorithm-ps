import sys
n, m = map(int, input().split())
squares = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
min_num = None
for i in range(n-7):
    for j in range(m-7):
        count1, count2 = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l-i-j) % 2 == 0 and squares[k][l] == 'B':
                    count1 += 1
                if (k+l-i-j) % 2 != 0 and squares[k][l] == 'W':
                    count1 += 1
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l-i-j) % 2 == 0 and squares[k][l] == 'W':
                    count2 += 1
                if (k+l-i-j) % 2 != 0 and squares[k][l] == 'B':
                    count2 += 1
        count1 = min(count1, 64-count1)
        count2 = min(count2, 64-count2)
        min_count = min(count1, count2)
        
        if min_num is None:
            min_num = min_count
        else:
            min_num = min_count if min_num > min_count else min_num

print(min_num)
