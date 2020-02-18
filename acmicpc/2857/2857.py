count = 0
for i in range(5):
    name = input()
    if 'FBI' in name:
        print(i+1, end=' ')
        count += 1
    if i is 4 and count == 0:
        print("HE GOT AWAY!")
