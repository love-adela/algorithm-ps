scale_num = list(map(int, input().split()))

if scale_num == sorted(scale_num, reverse=True):
    print('descending')
elif scale_num == sorted(scale_num):
    print('ascending')
else:
    print('mixed')
