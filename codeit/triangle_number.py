# Time Complexity : O(n) ... O(1) * n

def triangle_number(n):
    if n == 1:
        return 1
    return n + triangle_number(n - 1)

for i in range(1, 11):
    print(triangle_number(i))