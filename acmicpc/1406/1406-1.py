import sys
left_stack, right_stack = list(input()), list()
sys.stdin.readline()
for command in sys.stdin:
    if command[0] == 'L' and left_stack:
        right_stack.append(left_stack.pop())
    elif command[0] == 'D' and right_stack:
        left_stack.append(right_stack.pop())
    elif command[0] == 'B' and left_stack:
        left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[2])
print(''.join(left_stack + right_stack[::-1]))
