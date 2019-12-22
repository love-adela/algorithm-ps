import sys
sup = 10**9
T = int(sys.stdin.readline())
for _ in range(T):
    size = int(sys.stdin.readline())
    numbers = list(map(int,sys.stdin.readline().split()))
    cumulative = [sum(numbers[:i]) for i in range(size+1)]
    memo = [[0]*size for _ in range(size)]
    knuth = [[0]*size for _ in range(size)]
    for i in range(size):
        memo[i][i] = 0
        knuth[i][i] = i
    for i in range(size-1):
        memo[i][i+1] = cumulative[i+2] - cumulative[i]
        knuth[i][i+1] = i
    for j in range(2,size):
        for i in range(size):
            s = i
            e = i+j
            if e < size:
                tmp = sup
                for k in range(knuth[s][e-1],knuth[s+1][e]+1):
                    local_sum = memo[s][k] + memo[k+1][e]
                    if tmp > local_sum:
                        tmp = local_sum
                        knuth[s][e] = k
                memo[s][e] = cumulative[e+1] - cumulative[s] + tmp
    print(memo[0][size-1])
