a,b = input().split()
reverse = lambda n: int(n[::-1])
print(max(reverse(a), reverse(b)))
