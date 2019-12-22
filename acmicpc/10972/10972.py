# pandita's algorithm : https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

n = int(input())
permutations = list(map(int, input().split()))

def is_last_element(param:list)->bool:

