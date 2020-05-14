R, C, W = map(int, input().split())

def pascal(row, col):
    if col == 0:
        return 1
    if row == 1:
        return col
    return (row * pascal(row-1, col-1)// col)

print(pascal(R, C))
