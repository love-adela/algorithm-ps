from collections import Counter

def solution(participant:list, completion:list)->str:
    answer = ''

    runners = Counter(participant)
    for runner in completion:
        runners[runner] -= 1 
    for runner, count in runners.items():
        if count > 0:
            answer = runner 
            return answer


def test_solution():
    assert solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']) == 'leo'
    assert solution(
        ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
        ['josipa', 'filipa', 'marina', 'nikola']
    ) == 'vinko'
    assert solution(
        ['mislav', 'stanko', 'mislav', 'ana'],
        ['stanko', 'ana', 'mislav']
    ) == 'mislav'
print(test_solution())
