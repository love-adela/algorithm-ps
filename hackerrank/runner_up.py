if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


def runner_up(arr):
    max = 0
    runner_up = max

    for i in arr:
        if i > max:
            runner_up = max
            max = i
        elif i > runner_up and (i < max or max == runner_up):
            runner_up = i
    return runner_up


print(runner_up(arr))
