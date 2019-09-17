import sys
print(*map(sys.stdin.readline().rstrip().find, map(chr, range(97, 123))), sep=" ")
