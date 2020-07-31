input()
A = {int(param) for param in input().split()}
B = {int(param) for param in input().split()}
print(len(A-B))
for i in sorted(A-B):
    print(i, end = ' ')
