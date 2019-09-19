import sys
words = sys.stdin.readline().strip()
print(0 if len(words) == 0 else words.count(' ') +1)
