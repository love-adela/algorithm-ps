from itertools import combinations
s = input()
print(sorted([s[:com[0]][::-1]+s[com[0]:com[1]][::-1]+s[com[1]:][::-1] for com in combinations(range(1, len(s)), 2)])[0])

