flag = True
while flag:
    statement = input()
    if statement == 'END':
        flag = False
        break
    print(statement[::-1])

