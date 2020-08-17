base_dict = {'A': 'ACAG', 'G': 'CGTA', 'C':'ATCG', 'T': 'GAGT'}
n, s = input(), input()
current = s[-1]
for char in s[:-1][::-1]:
    index = 'AGCT'.find(current)
    current = base_dict[char][index]
print(current)
