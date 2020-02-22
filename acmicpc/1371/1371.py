s = ''
while True:
    try:
        s+= input()
    except:
        break
r = ['a', s.count('a')]
for i in range(98, 123):
    n = s.count(chr(i))
    if n > r[1]:
        r[0] = chr(i)
        r[1] = n
    elif n == r[1]:
        r[0] += chr(i)  
print(r[0])
