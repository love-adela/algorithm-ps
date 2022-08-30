while True:
    number = input()
    if number == '0':
        break

    blank = len(number)+1
    count = blank 
    for c in number:
        if c == '1':
            count += 2
        elif c == '0':
            count += 4
        else:
            count += 3
    print(count)
