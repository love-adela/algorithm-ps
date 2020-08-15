'''
1. N번 동안 맨 위에 있는 카드 버리고 출력하기
2. 제일 위의 카드 맨 밑으로 옮기기
'''

N = int(input())
numbers = [num+1 for num in range(N)]
while True:
    # 맨 위에 있는 카드를 한장 뽑아 출력
    pick, *numbers = numbers
    print(pick, end=' ')

    if len(numbers) == 0:
        break

    # 맨 위에 있는 카드 한장을 뽑아 맨 밑으로 넣음
    numbers = numbers[1:] + [numbers[0]]
