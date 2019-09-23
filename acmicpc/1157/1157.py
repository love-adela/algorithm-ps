words = input().upper()
letters = [words.count(chr(c)) for c in range(65, 91)]
m = max(letters)
if letters.count(m) == 1:
    print(chr(letters.index(m) + 65))
else:
    print('?')
