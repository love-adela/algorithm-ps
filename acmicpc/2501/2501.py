n, k = map(int, input().split())
gcd = []
def euclidean(a, b):
    if b == 0: 
        gcd.append(a)
        return gcd 
    else:
        return euclidean(b, a % b)
print(euclidean(n, k))
