c, r, k = [int(x) for x in input().strip().split()]
y, x = 0, 1
r_low, r_high = 1, r
c_low, c_high = 1, c
cur = 0

while r_low <= r_high and c_low < c_high:
    diff = k - cur
    if diff > r_high - r_low + 1:
        dist = r_high - r_low + 1
        y += dist
        cur += dist
        c_low += 1
    else:
        y += diff
        cur += diff
        break

    if r_low > r_high or c_low > c_high:
        break

    diff = k - cur
    if diff > c_high - c_low + 1:
        dist = c_high - c_low + 1
        x += dist
        cur += dist
        r_high -= 1
    else:
        x += diff
        cur += diff
        break

    if r_low > r_high or c_low > c_high:
        break

    diff = k - cur
    if diff > r_high - r_low + 1:
        dist = r_high - r_low + 1
        y -= dist
        cur += dist
        c_high += 1
    else:
        y -= diff
        cur += diff
        break

    if r_low > r_high or c_low > c_high:
        break

    diff = k - cur
    if diff > c_high - c_low + 1:
        dist = c_high - c_low + 1
        x -= dist
        cur += dist
        r_low += 1
    else:
        x -= diff
        cur += diff
        break

if cur == k:
    print(f'{x} {y}')
else:
    print(0)
