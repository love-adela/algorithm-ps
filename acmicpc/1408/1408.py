hc, mc, sc = map(int, input().split(':'))
ht, mt, st = map(int, input().split(':'))
time = 0
while not (hc == ht and mc == mt and sc == st):
    sc += 1
    time += 1
    if sc == 60:
        sc = 0
        mc += 1
        if mc == 60:
            mc = 0
            hc += 1
            if hc == 24:
                hc = 0
s = time % 60
m = (time//60)%60
h = (time//60)//60
print(f'{h:0>2}:{m:0>2}:{s:0>2}')
