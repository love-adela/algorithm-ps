N = int(input())
heights = [*map(int, input().split()), 0]

local_min = heights[0]
maximum = 0

for i in range(N):
    if heights[i+1] <= heights[i]:
        current = heights[i] - local_min
        if current > maximum:
            maximum = current
        local_min = heights[i+1]

print(maximum)
