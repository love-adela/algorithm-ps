def find_peak(matrix:list)->int:
    if len(matrix) == 0:
        return None
    if len(matrix) > 1:
        if len(matrix[0]) == 0:
            return None
    medium = len(matrix[0]) // 2
    maximum = find_max(matrix, medium) # 7
    
    column = [matrix[i][medium] for i in range(len(matrix))]
    index = find_max
    if matrix[i]< maximum < 
    print(matrix)
    print(medium)

    # 탐색 범위를 선정
    if len(matrix[0]) == 2:
        return matrix[N][medium]
    return maximum 
    if matrix[N][M-1] < matrix[N][M] > matrix[N][M+1]:
        return maximum[N][M]
    if matrix[N][M-1] >= matrix[N][M]:
        return find_peak([matrix[N][:M] for N in range(len(matrix))])
    if matrix[N][M+1] >= matrix[N][M]:
        return find_peak([matrix[N][M:] for N in range(len(matrix))])


def find_max(array:list, j=int):
    maximum = array[0][j]
    for i in range(len(array)):
        if array[i][j] > maximum:
            maximum = array[i][j] 
    return maximum

             
M, N = map(int, input().split())
columns = [list(map(int, input().split())) for _ in range(N)]
print(find_peak(columns))
