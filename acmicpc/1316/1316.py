count = 0
for _ in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        count += 1
print(count)
