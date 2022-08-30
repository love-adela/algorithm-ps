from itertools import accumulate

def get_accumulate_list(n):
    return list(accumulate(range(1, n+1)))

def calculate_score(score_str, n):
    score_str = score_str.replace(' ', '')
    accumulate_list = get_accumulate_list(n)
    scores = [accumulate_list[len(score)-1] for score in score_str.split('0') if len(score) != 0]
    return scores

n = int(input())
score_str = input()

print(sum(calculate_score(score_str, n)))
