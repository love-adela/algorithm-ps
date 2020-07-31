def is_empty(count:int)->bool:
    result = 0
    result += grid.count([0, 0, 0, 0, 0])
    if result >= 3:
        print(count)
        return True
    for i in range(5):
        for j in range(5):
            if grid[j][i] != 0:
                break
        else:
            result += 1
            if result >= 3:
                print(count)
                return True
    if grid[0][0] == 0 and grid[1][1] == 0 and grid[2][2] == 0 and grid[3][3] == 0 and grid[4][4] == 0:
        result += 1
        if result >= 3:
            print(count)
            return True
    if grid[0][4] == 0 and grid[1][3] == 0 and grid[2][2] == 0 and grid[3][1] == 0 and grid[4][0] == 0:
        result += 1
        if result >= 3:
            print(count)
            return True
    return False

grid = [input().split() for _ in range(5)]
count = 0 
c = False

for i in range(5):
    for e in input().split():
        count += 1
        state = False
        for j in range(5):
            for k in range(5):
                if e == grid[j][k]:
                    state = True
                    grid[j][k] = 0
                    c = is_empty(count)
                    break
            if state:
                break
        if c:
            break
    if c:
        break


