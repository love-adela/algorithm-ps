import sys
from collections import deque
read = lambda: sys.stdin.readline()

N, M = map(int, input().split())

#neighbor = [
#        [5],[], [3, 7], [2, 4, 8], [3, 9], [0, 6], [5, 7], [2, 6, 8], [3, 7, 9], [4, 8], 
#        [11, 15], [10, 12, 16], [11, 13, 17], [12, 14], [13], [10, 16], [11, 15, 17], [12, 16],
#        [19, 23], [18, 24], [21], [20, 22], [21, 23], [18, 22, 24], [19, 23]
#        ]
lst = []
for i in range(N):
    lst.append([param for param in input()])

print(lst)
node = [[(i*M)+j for j in range(M)] for i in range(N)] 
print(node)

