def solution(S):
    S = S.lower()

    dic = {}
    for i in S:
        if i == " ":
            continue
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1

    has_odd = False
    for i in dic.values():
        if i % 2 == 1:
            if not has_odd:
                has_odd = True
                continue
            return False
    return True

S = "tacocat"

print(solution(S))
