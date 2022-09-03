t = int(input())
for i in range(t):
    box = int(input())
    if box < 2:
        print('#' * box)
    else:
        print('#'*box)
        for _ in range(box-2):
            print('#', 'J'*(box-2), '#', sep='')
        print('#'*box)
    if i < t-1:
        print()

