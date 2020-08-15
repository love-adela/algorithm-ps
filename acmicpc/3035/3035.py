R, C, ZR, ZC = map(int, input().split())
for _ in range(R): # 각 행 별로 있는 문자를 R번 입력 받아서 변환하기
    letters = [param*ZC for param in input()]
    for _ in range(ZR): # ZR(세로)배로 늘리기
        print(''.join(letters))
