def staircase(n):

    for i in range (1, n+1):
        print(" " * (n - i) + "#" * i)

n = 6
print(staircase(6))