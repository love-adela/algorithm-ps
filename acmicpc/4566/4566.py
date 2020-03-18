import sys
while True: 
    input = sys.stdin.readline().strip()
    if input == 'END':
        break
    elif input[0] == '"':
        char = input[1:].split('" ')
        if len(char) > 1 and char[0] == char[1] and '"' not in char[0]:
            print(f'Quine({char[0]})')
        else:
            print('not a quine')
    else:
        print('not a quine')
