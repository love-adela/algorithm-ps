word = str(input())

while len(word) > 10:
    print(word[0:10], end='\n')
    word = word[10:]

if len(word) <= 10:
    print(word)


