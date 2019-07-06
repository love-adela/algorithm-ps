import sys
read = lambda: sys.stdin.readline()

N = int(read())
W = []
for i in range(N):
    edge = [int(x) for x in read().split()]
    W.append(edge)
    
visited_list = [[] for j in range(N)]
memo = [{} for i in range(N)]

for i in range(N):
    if W[i][0] > 0:
        visited_list[i].append(0)
        memo[i][0] = W[i][0]
    else:
        memo[i][0] = float('inf')
    for j in range(1, N):
        if W[i][j] > 0:
            visited_list[i].append(j)
    

def tsp(current_node, next_node):
    if next_node in memo[current_node].keys():
        return memo[current_node][next_node]
    else:
        temp_min = float('inf')
        for vertex in visited_list[current_node]:
            if 1<< vertex & next_node or next_node == 0:
                next_to_visit = next_node - (1<<vertex)
                temp_min = min(temp_min, tsp(vertex, next_to_visit) + W[current_node][vertex])
        memo[current_node][next_node] = temp_min
        return memo[current_node][next_node]
      
first_to_visit = ~(~0<<N)-1
print(tsp(0, first_to_visit))
