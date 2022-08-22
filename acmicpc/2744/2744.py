word = input()
letter_list = []
for letter in word:
    if letter.isupper():
        letter_list.append(letter.lower())
    else:
        letter_list.append(letter.upper())
print(''.join(letter_list))
