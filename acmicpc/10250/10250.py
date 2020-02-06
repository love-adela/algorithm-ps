T = int(input())
while T:
    H,W,N=map(int, input().split())
    hotel = []
    for i in range(W):
        for j in range(H):
            if (i+1) // 10 == 0:
                hotel.append(str(j+1)+'0'+str(i+1))
            else:
                hotel.append(str(j+1)+str(i+1))
    print(hotel[N-1])
    T -=1
