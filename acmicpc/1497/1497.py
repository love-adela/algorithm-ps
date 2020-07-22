import sys
from itertools import combinations

N, M = map(int, input().split()) 
guitar, yes_or_no = [], []
cases = []

# 기타, 곡 저장하기
for _ in range(N):
    count = 0
    g, yn = input().split()
    guitar.append(g)
    yes_or_no.append(yn)
s = [[string for string in param] for param in yes_or_no]
print(s)

# 모든 기타로 연주할 수 있는 곡의 개수 구하기
minimum = set()
for i in range(N):
    for j in range(M):
        if s[i][j] == 'Y':
            minimum.add(j+1)

# 기타로 구할 수 있는 모든 조합 구하기
for i in range(1, len(guitar)+1):
    cases.append(list(combinations(guitar, i)))

# 각 기타로 연주할 수 있는 곡의 개수 구하기
for i in range(len(cases)):
    for j in range(cases[i]):
        if s[i][j] == 'Y':
            
        
