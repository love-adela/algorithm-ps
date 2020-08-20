N = int(input())
"""
- [x] 반복을 마칠 수 있는 종료 조건 : 새가 0마리 일 때
- [x] 반복 조건 : 노래 1번 부터 가능할 때까지
- [x] 반복하는 동안 해야 하는 일 : 노래번호를+=1 해가면서 부르기 
- [x] 문제 조건 : if 새의 수 < 불러야 하는 수: 노래 1을 다시 부른다

"""
count = 0 # 새가 날아가기까지 걸리는 시간
song_number = 0
while True:
    count += 1
    song_number += 1 # 초기 노래 번호
    N -= song_number

    if N == 0:
        break
    if N <= song_number:
        song_number = 0
        continue
print(count)
