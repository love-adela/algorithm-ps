BST = [
    "*",
    ["+", [1, None, None], [2, None, None]],
    [3, None, None],
]

# Stack 쓰기
# Prefix
def dfs_prefix(tree:tuple):
    stack = [tree]

    while stack:
        node = stack.pop()
        value, left, right = node
        print(value, end=" ") # 1
        if right is not None:
            stack.append(right)            
        if left is not None:
            stack.append(left)
        

def dfs_infix(tree:tuple): 
    if tree is None:
        return
    dfs_infix(tree[1])
    print(tree[0], end=" ")
    dfs_infix(tree[2])


# Postfix
def dfs_postfix(tree:tuple):
    if tree is None:
        return None
        
    dfs_postfix(tree[1])
    dfs_postfix(tree[2])
    print(tree[0], end=" ")


# Test
print("infix : ", end=" ")
dfs_infix(BST)

print("\nprefix : ", end=" ")
dfs_prefix(BST)

print("\npostfix : ", end=" ")
dfs_postfix(BST)