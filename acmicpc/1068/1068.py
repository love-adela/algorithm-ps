def preorder(node):
    global count
    if node.child == []:
        count +=1 
    for child in node.child:
        preorder(tree[child])


class Node:
    def __init__(self):
        self.child = []
    def set_child(self, node):
        self.child.append(node)
    def remove_child(self, node):
        self.child.remove(node)

N = int(input())
tree = [Node() for _ in range(N)]
count = 0 
parent = list(map(int, input().split()))
for i in range(N):
    if parent[i] != -1:
        tree[parent[i]].set_child(i)

if N!= 1:
    i = int(input())
    if parent[i] == -1:
        count = 0 
    else:
        tree[parent[i]].remove_child(i)
        preorder(tree[parent.index(-1)])
print(count)
