a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

cost = a * p
if c < p:
    y = b + ((p - c) * d)
else:
    y = b

if cost < y:
    print(cost)
else:
    print(y)
