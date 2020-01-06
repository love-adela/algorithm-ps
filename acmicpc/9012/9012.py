import sys
T = int(input())

def is_vps(string:str)->str:
    characters = [param for param in string]
    index = 0
    
    while len(characters) != 0:
        if index < 0:
            break
        c = characters.pop()

        if c == '(':
            index -= 1
        elif c == ')':
            index += 1

    if index == 0:
        return 'YES' 
    else:
        return 'NO'

while T:
    parentheses = sys.stdin.readline()
    print(is_vps(parentheses))
    T -=1
