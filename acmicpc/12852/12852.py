d, p = [[int(input())]], []
while True:
    d2 = []
    for i in d:
        j=i[-1]
        if j==1:
            print(len(i)-1)
            print(' '.join(map(str, i)))
            exit()
        if j%3==0 and j//3 not in p:
            d2+=[i+[j//3]]
            p+=[j//3]
        if j%2==0 and j//2 not in p:
            d2+=[i+[j//2]]
            p+=[j//2]
        if j-1 not in p:
            d2+= [i+[j-1]]
            p+=[j-1]
    d=d2
            
