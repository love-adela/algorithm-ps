s = ''
for t in input().split('<'):
    if '>' in t:
        x, y = t.split('>')
        s+= '<' + x + '>' + ' '.join(map(lambda t: t[::-1], y.split(' ')))
    else: s += ' '.join(map(lambda t: t[::-1], t.split(' ')))
print(s)
