# A -> B (90도로 돌렸을 때)
A = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
temp = [[], [], []]
def rotate(lst:list, new:list)->list:
    for i in range(len(lst)):
        for j in range(len(lst)):
            new[i], new[j] = lst[j], lst[2-i]
    print(new)
    return new

B = rotate(A, temp)
print(B)
