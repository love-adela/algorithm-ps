T= int(input())
for i in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    for j in range(N-2): # 0, 1, 2
        avg = (heights[j]+heights[j+2])/2 #(0,2), (1,3), (2, 4)
        if heights[j+1] >= avg:
            heights[j+1] = avg
    print(f'Case #{i+1}: {heights[-2]:.6f}')

