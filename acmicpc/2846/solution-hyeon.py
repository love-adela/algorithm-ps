N = int(input())
heights = [*map(int, input().split()), 0]

local_min = heights[0]
def for_each(i):
    global local_min
    ret = heights[i] - local_min
    local_min = heights[i+1]
    return ret

print(max(for_each(i) for i in range(N) if heights[i+1] <= heights[i]))
