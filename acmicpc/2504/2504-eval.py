import sys

s = sys.stdin.readline().strip()
try: 
    eval('0,' + s.replace(')', '),').replace(']','],'))
    s = s.replace('()', '(1)')
    s = s.replace('[]', '[1]')
    s = s.replace('(', '+2*(')
    s = s.replace('[', '+3*(')
    s = s.replace(']', ')')
    print(eval(s))
except:
    print(0)
    exit(0)
