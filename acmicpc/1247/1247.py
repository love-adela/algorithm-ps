for _ in range(3):
    n = int(input())
    test_list = [int(input()) for _ in range(n)]
    if sum(test_list) == 0:
        print('0')
    elif sum(test_list) > 0:
        print('+')
    else:
        print('-')
