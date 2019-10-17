from collections import Counter

def solution(participant:list, completion:list)->str:
    return next((Counter(participant) - Counter(completion)).elements())


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
