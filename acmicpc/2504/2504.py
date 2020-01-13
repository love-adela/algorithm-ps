def get_open(c:str):
    if c == ')':
        return '('
    if c == ']':
        return '['
    return None

def get_mul(c:str):
    if c == ')':
        return 2
    if c == ']':
        return 3
    return 0

def main(string):
    s = []
    v = []
    ans = 0
    for c in string:
        if c in '([':
            s.append(c)
            v.append(0)
        else:
            if not s:
                return 0
            if s[-1] != get_open(c):
                return 0
            s.pop()
            value = v.pop()
            if value == 0:
                value = 1
            value *= get_mul(c)
            if not v:
                ans += value
            else:
                value += v.pop()
                v.append(value)
    if s:
        return 0
    return ans
print(main(input()))
