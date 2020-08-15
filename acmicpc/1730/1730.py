# boj.kr/1730 판화
"""
* 목판의 크기 : n (2<=n<=100)
* 로봇팔을 움직이는 명령: U, D, L, R (문자열로 공백없이 1000만큼 주어짐)
"""
n = int(input())
s = input()

count = [[0 for _ in range(n)] for _ in range(n)]
grid = [['.' for _ in range(n)] for _ in range(n)]
cmd = [param for param in s]
length = len(s)

def main():
    for k in range(length):
        for i in range(n+1):
        #TODO:  s 의 길이가 grid의 내부 배열보다 길 경우, 다음 배열로 넘어가는 경우 처리
            for j in range(n+1):
                if cmd[k] == 'D':
                    grid[i][j] = '|'
                    count[i][j] += 1
                    return grid
                elif cmd[k] == 'U':
                    grid[i][j] = '|'
                    count[i][j] += 1
                    return grid
                elif cmd[k] == 'L':
                    grid[i][j] = '-'
                    count[i][j] += 1
                    return grid
                else:
                    grid[i][j] = '-'
                    count[i][j] += 1
                    return grid
        
print(main())
print(count)


