import sys
T = int(input())
string = sys.stdin.read().splitlines()
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = []

for i in range(T):
    result = 0
    for c in s:
        if string[i].find(c) == -1:
            result += ord(c)
    l.append(result)
print('\n'.join(map(str, l)))
