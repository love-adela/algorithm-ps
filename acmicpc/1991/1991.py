N= int(input())
nodes = {i:[] for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

# Generate Tree
for _ in range(N):
    node, left, right = map(str, input().split())
    nodes[node] += [left, right]


# Preorder Traversal
def preorder(nodes:dict, root:str)->str:
    stack = [root]
    result = ''

    while stack:
        node = stack.pop()
        result += node

        if nodes[node][1] != '.':
            stack.append(nodes[node][1])
        if nodes[node][0] != '.':
            stack.append(nodes[node][0])

    return result


# Inorder Traversal
def inorder(nodes:dict, root:str)->str:
    stack = [root]
    result = ''

    while stack:
        if nodes[stack[-1]][0] != '.' and nodes[stack[-1]][0] not in result:
            stack.append(nodes[stack[-1]][0])
        elif stack[-1] in result:
            stack.append(nodes[stack[-1]][1])
        else:
            node = stack.pop()
            result += node
            if nodes[node][1] != '.':
                stack.append(nodes[node][1])
    return result


# Postorder Traversal
def postorder(nodes:dict, root:str)->str:
    stack = [root]
    result = ''
    
    while stack:
        if nodes[stack[-1]][0] != '.' and nodes[stack[-1]][0] not in result:
            stack.append(nodes[stack[-1]][0])
            
        elif nodes[stack[-1]][1] == '.' or nodes[stack[-1]][1] in result:
            result += stack.pop()
            
        else:
            stack.append(nodes[stack[-1]][1])
            
    return result

print(preorder(nodes, "A"))
print(inorder(nodes, "A"))
print(postorder(nodes, "A"))
