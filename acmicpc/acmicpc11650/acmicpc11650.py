import sys

N = int(sys.stdin.readline())
coordinates = []

for _ in range(N):
    coordinates.append([int(param) for param in input().split()])
coordinates.sort(key=lambda x: (x[0], x[1]))

for coordinate in coordinates:
    print(*coordinate) # print(coordinate[0], coordinate[1])

    
