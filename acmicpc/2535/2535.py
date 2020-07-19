N = int(input())
students = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: -x[2])
print(*students[0][:2])
print(*students[1][:2])

if students[0][0] == students[2][0]:
    print(*students[3][:2])
else:
    print(*students[2][:2])

