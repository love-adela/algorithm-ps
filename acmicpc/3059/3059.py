T = int(input())
for _ in range(T):
    s = input()
    result = 0

    for i in range(ord('A'), ord('Z')+1):
        for j in range(len(s)):
            if ord(s[j]) == i:
                result += ord(s[j])
                break
    print(2015 - result)
