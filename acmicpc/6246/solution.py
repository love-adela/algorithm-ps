# boj.kr/6246
"""
- [x] 반복해야 하는 일 : interval개씩 띄어서 풍선 놓기
- [x] 반복해야 하는 일을 종료하는 조건 : Q == 0
  - [x] 각각의 Q번 동안 이뤄지는 행위를 종료하는 조건 : 슬롯 번호 > N
  - [x] 시작 지점 : start, start_idx
  - [x] 각 slot에 풍선을 놓는 행위 : slot_list[i] = 1

- [x] slot = [0, 0, 0, 0, ..., 0] 으로 표현 # len(slot) = N
- [x] slot 파라미터가 0이면 비어있는 것으로 카운트
"""
def put_ballons(start_idx:int, interval:int, slot_list:list)->list:
    for i in range(start_idx, N+1, interval):
        slot_list[i-1] = 1
    return slot_list

N, Q = map(int, input().split())
slot = [0 for _ in range(N)]
while Q:
    start, interval = map(int, input().split())
    # 풍선을 꽂는 함수
    put_ballons(start, interval, slot)
    Q -= 1

count = 0
for param in slot:
    if param == 0:
        count += 1
print(count)
