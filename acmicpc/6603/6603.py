# https://docs.python.org/3/library/itertools.html#itertools.combinations
import sys
from itertools import combinations

while True:
    case = list(map(int, sys.stdin.readline().split()))
    if case[0] == 0:
        break
    for i in combinations(case[1:], 6):
        print(' '.join(map(str, i)))
    print()
    

