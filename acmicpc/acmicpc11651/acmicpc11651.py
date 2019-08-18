import sys

N = int(sys.stdin.readline())
coordinates = []

for _ in range(N):
    coordinates.append([int(param) for param in input().split()])
coordinates.sort(key=lambda y: (y[1], y[0]))

for coordinate in coordinates:
    print(*coordinate)
