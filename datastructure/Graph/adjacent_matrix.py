# Nested Matrix로 구현
a, b, c, d, e, f = range(6)
N = [[0, 1, 1, 1, 0, 1], [1, 0, 0, 1, 0, 1], [1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0]]
print(N[a][b]) # 1
print(N[a][e]) # 0
print(sum(N[f])) # True

# 간선이 존재하지 않는 경우
_ = float('inf')
N = [[_, 2, 1, 4, _, 1], [4, _, _, 1, _, 4], [1, 1, _, 2, 4, _], [3, _, _, _, 2, _], [3, 4, 1, _, _, _], [1, 2, _, 4, 3, _]]
print(N[a][b] < _) # True
print(N[f])
print([1 for w in N[f] if w < _])
print(sum(1 for w in N[f] if w < _)) # 4
