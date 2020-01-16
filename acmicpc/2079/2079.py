import sys

def palindrome_with_stack(string:str)->str:
    if string == string[::-1]:
        return 1
    else:
        s = Stack()
        result = ''
        for c in string:
            s.push(c)

        while not s.is_empty():
            result += s.pop()
        return result


