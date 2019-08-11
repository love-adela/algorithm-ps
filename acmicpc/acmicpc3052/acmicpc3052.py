rest_lst = []
for _ in range(10):
    n = int(input())
    rest_lst.append(n % 42)

print(len(set(rest_lst)))
