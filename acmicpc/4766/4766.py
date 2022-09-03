data = []
while True:
    temp = float(input())
    if temp == 999:
        break
    data.append(temp)

for i in range(1, len(data)):
    print('%.2f' % (data[i] - data[i-1]))

