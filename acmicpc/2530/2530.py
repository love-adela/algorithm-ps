A, B, C = map(int, input().split())
C += int(input())

exc_s = C // 60 
if exc_s >= 1:
    C -= 60 * exc_s
    B += 1 * exc_s

exc_m = B // 60
if exc_m >= 1:
    B -= 60 * exc_m
    A += 1 * exc_m

exc_h = A // 24
if exc_h >= 1:
    A -= 24 * exc_h

print(A, B, C)

