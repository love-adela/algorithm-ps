import sys

sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())


def get_preorder(inorder_start, inorder_end, postorder_start, postorder_end):
    if postorder_start > postorder_end:
        return 
    if inorder_start > inorder_end:
        return 

    root = postorder[postorder_end]
    print(root, end=' ')

    inorder_root = inposition[root]
    left_size = inorder_root - inorder_start

    get_preorder(inorder_start, inorder_root-1, postorder_start, postorder_start + left_size-1)
    get_preorder(inorder_root+1, inorder_end, postorder_start+left_size, postorder_end-1)


inorder = list(map(int, sys.stdin.readline().split(' ')))
postorder = list(map(int, sys.stdin.readline().split(' ')))
inposition = [0] * (max(inorder) + 1)
inposition = [0] * (max(inorder) + 1)

for i, v in enumerate(inorder):
    inposition[v] = i

get_preorder(0, n - 1, 0, n - 1)
