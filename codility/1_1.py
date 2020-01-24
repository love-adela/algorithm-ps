def solution(S):
    #hash_map
    dic = {}
    for i in S:
        #get : 문자가 없는 경우 return을 시킬 수 있기 때문에 사용
        if dic.get(i):
            return True
        dic[i] = 1
    return False

S = "codility"
print(solution(S))
