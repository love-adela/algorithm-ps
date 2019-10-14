import sys
read = lambda: sys.stdin.readline().rstrip('\n')
octal = read()
print(bin(int(octal,8))[2:])
