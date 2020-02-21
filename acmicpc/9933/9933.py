N = int(input())
words = [input() for param in range(N)]
for word in words:
    if word[::-1] in words:
        print(len(word), end=' ')
        print(word[len(word) // 2])
        break

