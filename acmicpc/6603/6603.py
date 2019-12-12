# https://docs.python.org/3/library/itertools.html#itertools.combinations
import sys
from itertools import combinations

flag = True
while flag:
    elem = list(map(int, sys.stdin.readline().strip().split()))
    e = int(elem[0])
    if e == 0:
        flag = False
        break
    for i in combinations(elem[1:], 6):
        print(' '.join(map(str, i)))
    print()
