import math

def turret(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # 무한히 만나는 경우
    if r1 == r2 and d == 0:
        return -1

    # 두 원이 한 점에서 접하는 경우
    if abs(r1 - r2) == d or r1 + r2 == d:
        return 1

    # 두 원이 두 점에서 만나는 경우
    if abs(r1 - r2) < d < r1 + r2:
        return 2
    
    # 두 원이 만나지 않는 경우
    return 0


numbers = int(input())

for i in range(0, numbers):
    answer = turret(i)
    print(answer)
