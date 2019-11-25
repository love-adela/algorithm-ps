def get_hansu(N):
    count = 0 
    for i in range(1, N+1):
        if i<100:
            count+=1
        elif 99<i<1000:
            if (i//100)+(i%10) == 2*(i//10-(i//100)*10):
                count += 1
    return count

print(get_hansu(int(input())))

