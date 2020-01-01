from sys import stdin
next(stdin)
for line in stdin:
    a, b = map(int, line.split())
    result = [(a**i)%10 for i in range(1, 5)][(b%4)-1]
    print(result if result != 0 else 10)
