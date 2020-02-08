import sys
a, b = map(int, sys.stdin.readline().split())
# a와 b사이에 있는 4 이상 짝수의 합
# 등차수열의 합을 이용
count = 0
for i in range(a, b+1):
    if i >= 4 and i % 2 == 0:
        count += i
print(count)
