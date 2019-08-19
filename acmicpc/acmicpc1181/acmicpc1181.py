import sys

N = int(sys.stdin.readline())

words = set() 
for _ in range(N):
    words.add(sys.stdin.readline())

words = list(words)
words.sort()
words.sort(key=lambda x:len(x))
print(''.join(words))
