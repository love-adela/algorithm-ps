# 루트 노드 -> 왼쪽 노드 -> 오른쪽 노드 순으로 방문한다.
def preorder(root):
    if root != 0:
        yield root.value
        preorder(root.left)
        preorder(root.right)

