def count_vowl(sentence):
    vowl = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    cnt = 0
    for char in sentence:
        if char in vowl:
            cnt += 1
    return cnt

while True:
    input_sentence = input()

    if input_sentence == '#':
        break
    print(count_vowl(input_sentence))




