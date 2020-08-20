# boj.kr/1173
N, m, M, T, R = map(int, input().split())
"""
- 초기맥박(x) : 70
- 운동할 때 맥박(T)이 25씩 증가
- 휴식할 때 맥박(R)이 15씩 감소

- 맥박이 m, 70 보다 낮아지지 않는다
- 맥박이 M보다 높아지지 않는다
----------------------------------------
# 반복적으로 상태가 바뀌는 경우
State = StartState
while not IsEnd(State):
	Logic(State)
	State = Next(State)
"""
# 시작 상태, 초기맥박 x : m, 최소시간 min_time: 0
x, min_time = m, 0
while N:
    # 로직
    min_time += 1
    # 운동을 계속 하는 상태: (맥박 + 운동 맥박 증가량) <= 최대 맥박
    if x + T <= M:
        x += T
        N -= 1
        continue
    # 휴식을 계속 하는 상태 : (맥박 - 휴식 맥박 감소량 >= m)
    if x - R >= m:
        x -= R
    else:
        x = m
    # 운동을 할 수 없는 종료 상태 : (초기 맥박 + 운동 맥박 증가량) > 최대 맥박
    if x == m and x+T> M:
        min_time = -1
        break

print(min_time)
