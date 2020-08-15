len_a, len_b= map(int, input().split())
A = {param for param in input().split()}
B = {param for param in input().split()}
print(len(A ^ B))



