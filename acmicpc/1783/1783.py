N, M = map(int, input().split())

def main():
    if N == 1:
        return 1
    elif N == 2:
        return min(4, (M+1)//2)
    elif N >= 3:
        if M >= 7:
            return M -2
        else:
            return min(4, M)

print(main())
