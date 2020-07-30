from itertools import combinations
word = input()
lst = []
for item in combinations(range(1, len(word)), 2):
    item = word[:item[0]][::-1] + word[item[0]: item[1]][::-1] + word[item[1]:][::-1]
    lst.append(item)
print(sorted(lst)[0])

