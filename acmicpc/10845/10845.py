N = int(input())

def main(lst:list):
    cmd = input()
    print(cmd)
    if cmd == "pop":
        if len(lst) == 0:
            return -1
        lst.pop(lst[0])
        return lst[0]
    elif cmd == "size":
        return len(lst)
    elif cmd == "empty":
        if len(lst) == 0: return 1
        else: return 0
    elif cmd == "front":
        if len(lst) == 0:
            return -1
        return lst[0]
    elif cmd == "back":
        if len(lst) == 0:
            return -1
        return lst[-1]
    else:
        elem = int(input().strip('push '))
        lst.append(elem)
        print(f'lst:{lst}')
        return elem 

while N:
    params = []
    print(main(params))
    N -= 1
