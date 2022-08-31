p, q, r = map(int, input().split())
result = ''
if p + q == r:
    result = f'{p}+{q}={r}'
if p - q == r:
    result = f'{p}-{q}={r}'
if p * q == r:
    result = f'{p}*{q}={r}'
if p / q == r:
    result = f'{p}/{q}={r}'
if p == q + r:
    result = f'{p}={q}+{r}'
if p == q - r:
    result = f'{p}={q}-{r}'
if p == q * r:
    result = f'{p}={q}*{r}'
if p == q / r:
    result = f'{p}={q}/{r}'
print(result)
