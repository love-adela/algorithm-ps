N = int(input())
heights = [int(param) for param in input().split()]

current_sub = [heights[0]] 
last = heights[0]
maximum = 0

for item in heights[1:]:
    if item <= last:
        diff = current_sub[-1] - current_sub[0]
        maximum = max(maximum, diff)
        current_sub = []
    current_sub.append(item)
    last = item

diff = current_sub[-1] - current_sub[0]
maximum = max(maximum, diff)
print(maximum)
