from sys import setrecursionlimit

"""
1. N번 동안 맨 위에 있는 카드 버리고 출력하기
2. 제일 위의 카드 맨 밑으로 옮기기
"""

def move_top_to_bottom(num_lst:list)->list:
    return num_lst[1:] + [num_lst[0]]

def discard_top_card(num_lst:list)->list:
    return num_lst[1:]


def main(numbers):
    print(numbers[0], end=' ')
    if len(numbers) == 1:
        return 
    new_numbers = discard_top_card(numbers)
    final_numbers = move_top_to_bottom(new_numbers)
    return main(final_numbers)

setrecursionlimit(1010)
N = int(input())
numbers = [int(num) for num in range(1, N+1)]
main(numbers)
