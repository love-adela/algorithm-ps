N = int(input())
cnt_cute, cnt_not_cute = 0, 0 

while N:
    if int(input()) == 1:
        cnt_cute += 1
    else:
        cnt_not_cute += 1
    N -=1
if cnt_cute > cnt_not_cute: print('Junhee is cute!')
else: print('Junhee is not cute!')

