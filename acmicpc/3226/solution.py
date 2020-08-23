# boj.kr/3226

N = int(input())
total_cost = 0 
for _ in range(N):
    time_str, delta = input().split()
    delta = int(delta)
    hour, minute = map(int, time_str.split(':'))
    minute += 60 * hour
    for m in range(minute, minute+delta):
        if 420 <= m < 1140:
            total_cost += 10
        else:
            total_cost += 5
print(total_cost)
