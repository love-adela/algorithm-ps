import sys
read = lambda: sys.stdin.readline()

num = dict()
for a in map(int, read().split()):
    try:
        num[a] += 1
    except:
        num[a] = 1

if len(num) == 1:
    print(10000 + sum(num.keys())*1000)
elif len(num) == 2:
    print(1000 + sorted(num, key= lambda x: num[x])[1]*100)
elif len(num) == 3:
    print(sorted(num)[-1]*100)
