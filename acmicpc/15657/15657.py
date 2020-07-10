N, M = map(int, input().split())

def get_seq(selected, length):
    if length == M:
        print(*selected)
    elif length == 0:
        for item in sequence:
            get_seq(selected + [item], length +1)
    else:
        for item in sequence:
            if item >= selected[-1]:
                get_seq(selected+[item], length+1)

sequence = sorted([int(param) for param in input().split()])
get_seq([], 0)
