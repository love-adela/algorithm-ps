word = input()
count = 0 
for c in word:
    if ord(c) <= 82:
        count += (((ord(c) - ord('A')) // 3) + 3)
    elif c == 'S':
        count += 8
    elif c == 'T' or c == 'U' or c == 'V':
        count += 9
    elif c == 'W' or c == 'X' or c == 'Y' or c == 'Z':
        count += 10
print(count)
