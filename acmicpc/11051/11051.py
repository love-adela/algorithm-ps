def pascal(row, column):
    if column == 0:
        return 1
    if row == 0:
        return column
    return (row * pascal(row-1, column-1)) // column

row, column = map(int, input().split())
print(pascal(row, column)%10007)
