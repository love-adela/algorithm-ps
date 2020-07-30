n = input()
count = 0
cards = []
for ch in n:
    if ch == '9': ch = '6'
    if ch not in cards:
        tmp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '6']
        tmp.remove(ch)
        cards.extend(tmp)
        count += 1
    else:
        cards.remove(ch)
print(count)
