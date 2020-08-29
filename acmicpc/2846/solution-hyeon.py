N = int(input())
heights = [int(param) for param in input().split()]

current_sub = [] 
last = 0
maximum = 0
for item in heights:
    if item <= last:
        diff = current_sub[-1] - current_sub[0]
        maximum = max(maximum, diff)
        current_sub = []
    current_sub.append(item)
    last = item
diff = current_sub[-1] - current_sub[0]
maximum = max(maximum, diff)
print(maximum)
