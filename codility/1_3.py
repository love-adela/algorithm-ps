def solution(S):

    rs = ""

    for i in S:
        if i != " ":
            rs += i
        else:
            rs += "%20"
    return rs

S = "Mr John Smith"

print(solution(S))
