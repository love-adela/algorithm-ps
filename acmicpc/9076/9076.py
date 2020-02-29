T = int(input())
while T:
    grades = list(map(int, input().split()))
    grades.remove(max(grades))
    grades.remove(min(grades))

    if max(grades) - min(grades) >=4:
        print('KIN')
    else:
        print(sum(grades))
    T -=1
