s = input()
stack = []
length = len(s) # 21

i = 0
while i < length:
    if s[i] == '<':
        while i < length and s[i] != '>':
            print(s[i], end='')
            i += 1
        if s[i] == '>':
            print(s[i], end='')
            i += 1
    else:
        while i < length and s[i] != '<' and s[i] != ' ':
            stack.append(s[i])
            i += 1
        while len(stack) != 0:
            print(stack[-1], end='')
            stack.pop()
        if i < length and s[i] == ' ':
            print(s[i], end='')
            i += 1
print()
