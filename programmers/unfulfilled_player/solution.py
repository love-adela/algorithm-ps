def solution(participant:list, completion:list)->str:
    answer = ''
    runners = {}
    for p in participant:
        runners[p] = runners.get(p, 0) + 1
    for p in completion:
        runners[p] -= 1 
    for p, c in runners.items():
        if c > 0:
            answer = p
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
