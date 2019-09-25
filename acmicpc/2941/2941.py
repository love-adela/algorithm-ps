word = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for param in c:
    word = word.replace(param, '/')
print(len(word))
