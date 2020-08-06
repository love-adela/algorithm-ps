# boj.kr/6986 절사평균
import sys
read = lambda: sys.stdin.readline()
N, K = map(int, input().split())
data = sorted([float(read())*10 for _ in range(N)])
trimmed_data = data[K:N-K]

def get_trimmed_mean():
    answer = sum(trimmed_data) / len(trimmed_data)
    return '{:.2f}'.format(round(answer*0.1, 2))

def get_adjusted_mean():
    adjusted_data = [trimmed_data[0]] * K + trimmed_data + [trimmed_data[-1]] * K
    answer = sum(adjusted_data) / N
    return '{:.2f}'.format(round(answer*0.1, 2))

print(get_trimmed_mean())
print(get_adjusted_mean())
