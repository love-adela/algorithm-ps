N, M = map(int, input().split())

def dfs(selected, length):
    if length == M:
        print(' '.join(list(map(str, selected))))
    else:
        if length == 0:
            for item in sequence:
                dfs(selected + [item], length+1)
        else:
            for item in sequence:
                if item > selected[-1]:
                    dfs(selected+[item], length+1)

sequence = sorted([int(param) for param in input().split()])
dfs([], 0)
