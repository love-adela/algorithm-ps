# a와 b사이에 있는 4 이상 짝수의 합
# 등차수열의 합을 이용

import sys
a, b = map(int, sys.stdin.readline().split())
if a % 2 != 0: a += 1
if b % 2 != 0: b -= 1
total = ((a + b) //2)*(b//2-a//2+1)
if a <= 2 and b >=2:
    print(total-2)
else:
    print(total)
