N, M = map(int, input().split())

def get_seq(included, length):
    if length == M: 
        print(' '.join(list(map(str, included))))
    else:
        for item in sequence:
            get_seq(included + [item], length+1)

sequence = sorted([int(param) for param in input().split()])
get_seq([], 0)
