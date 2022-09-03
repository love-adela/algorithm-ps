n = int(input())
for i in range(n):
    s = ''
    print(f'String #{i+1}')
    for char in input():
        char = ord(char) + 1
        if char == 91:
            s += 'A'
        else:
            s += chr(char)
    print(s+('\n' if i!= n-1 else ''))
