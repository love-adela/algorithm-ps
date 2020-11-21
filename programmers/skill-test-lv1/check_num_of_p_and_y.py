# https://programmers.co.kr/learn/courses/30/lessons/12916
def solution(s:str)->bool:
    s = s.lower()
    return s.count('p') == s.count('y')

# Test
# s = 'pPoooyY'
# s = 'Pyy'
s = 'pPPooyYy'
print(solution(s))

