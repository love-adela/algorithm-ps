n = int(input())

name_dict = {}
letters = ""
while n:
    name = input()
    first_letter = name[0]
    count = name_dict.get(first_letter, 0)
    count += 1
    name_dict[first_letter] = count
    if count == 5:
        letters += first_letter
    n -= 1

if len(letters) > 0:
    print(''.join(sorted(letters)))
else:
    print('PREDAJA')
