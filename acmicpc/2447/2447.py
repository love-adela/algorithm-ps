import sys

num = int(input())

def get_star(i, j):
    while i != 0:
        if i % 3 == 1 and j % 3 == 1:
            sys.stdout.write(' ')
            return None
        i=i//3
        j=j//3
    sys.stdout.write('*')

for i in range(num):
    for j in range(num):
            get_star(i, j)
    sys.stdout.write('\n')
