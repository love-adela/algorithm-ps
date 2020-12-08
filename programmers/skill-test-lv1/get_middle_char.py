def solution(s):
    length = len(s)
    return s[length // 2] if length % 2 != 0 else s[(length // 2)-1:(length // 2)+1]

# Test
# s = 'abcde'
s = 'qwer'
print(solution(s))

#5 -> 2
#4 -> [1:3] # 1, 2
