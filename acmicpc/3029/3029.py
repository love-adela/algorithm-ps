h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

t1 = 3600 * h1 + 60 * m1 + s1
t2 = 3600 * h2 + 60 * m2 + s2

if t1 < t2:
    result = t2 - t1
else:
    result = t2 + 24*3600 -t1

h3 = result // 3600
result %= 3600
m3 = result // 60
result %= 60
s3 = result

print(f"{h3:02d}:{m3:02d}:{s3:02d}")
