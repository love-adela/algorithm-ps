n = int(input()) # n = 18

bag = 0

while n > 0:
    if n % 5 != 0: # n이 5의 배수가 아닐 때
        n -= 3
        if n < 0:
            bag = -1
            break
        bag += 1

    elif n % 5 != 0 and n % 3 !=0: # n이 5의 배수도 아니고 3의 배수도 아닐 때
        bag = -1

    elif n % 5 == 0: # n이 5의 배수일 때
        bag += 1
        n -= 5
print(bag)





