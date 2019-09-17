n = int(input())

sequence = [input() for _ in range(n)]

for elem in sequence:
    o = elem.split('X')
    o_list = [len(x)*(len(x)+1)//2 for x in o]
    print(sum(o_list))
