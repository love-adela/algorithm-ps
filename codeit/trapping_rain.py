def trapping_rain(buildings:list)->int:
    
    height = buildings[1]
    for i in range(1, len(buildings)-1):
        print()
        height = max(height, buildings[i])
        print(f'{i} 번째 {height}')
    return height


# print(trapping_rain([4, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
