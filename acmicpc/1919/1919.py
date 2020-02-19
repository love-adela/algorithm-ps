f,s = [0 for _ in range(26)], [0 for _ in range(26)]
first, second = input(), input()
for i in range(len(first)):
    f[ord(first[i]) - 97] += 1
for i in range(len(second)):
    s[ord(second[i]) - 97] += 1
print(sum([abs(f[i]-s[i]) for i in range(26) if f[i] != s[i]]))
