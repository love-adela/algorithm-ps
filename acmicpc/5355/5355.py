T = int(input())
for _ in range(T):
    oper = list(map(str, input().split()))
    answer = 0
    for i in range(len(oper)):
        if i == 0:
            answer += float(oper[i])
        else:
            if oper[i] == '#':
                answer -= 7
            elif oper[i] == '%':
                answer += 5
            else:
                answer *= 3
    print('%0.2f' %answer)
