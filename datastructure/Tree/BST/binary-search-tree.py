TABLE = [
    ('elephant', '코끼리'),
    ('cat', '고양이'),
    ('bird', '새'),
    ('dog', '개'),
    ('tiger', '호랑이'),
    ('zebra', '얼룩말'),
]

BST = [
    0,
    [1, [2, None, None], [3, None, None]],
    [4, None, [5, None, None]],
]


# ======================================================================

def find(tree: tuple, query: str):
    if tree is None:
        return None
    
    # Invariant : Tree = Tuple
    idx, left, right = tree
    key, value = TABLE[idx]

    if key < query:
        return find(right, query)
    elif key > query:
        return find(left, query)
    else: 
        return value

while True:
    query = input('찾을 값을 입력하세요: ')
    result = find(BST, query)
    print(repr(result))
    print()

# ======================================================================
def insert(tree: tuple, new_value: str) -> tuple:
    new_tree = insert(tree, new_value)

    if tree is None:
        return new_tree
        
    # Invariant : Tree = Tuple
    if new_value <= tree.query:
        if tree.left:
            insert(tree.left, new_value)
        else:
            tree.left = new_value
    elif new_value > tree.query:
        if new_value.right:
            insert(tree.right, new_value)
        else:
            new_value.right = new_value

while True:
    new_value = input('새로 넣을 값을 입력하세요: ')
    result = insert(BST, new_value)
    print(repr(result))
    print()

# ======================================================================
def delete(tree: tuple, deletion_value: str) -> tuple:
    new_tree = delete(tree, deletion_value)
    if tree is None:
        return new_tree
    
    _ = find(tree, deletion_value)

    idx, left, right = tree
    key, deletion_value = TABLE[idx]
    child = tree.right

    if deletion_value.left is not None and deletion_value.right is not None:
        child = tree.right
        while child.left is not None:
            child = child.left

while True:
    deletion_value = input('삭제할 값을 입력하세요: ')
    result = delete(BST, deletion_value)
    print(repr(result))
    print()


# ======================================================================
# TODO
def find_predecessor():
    pass


# ======================================================================
# TODO : 정해진 갯수만큼 가져오기
def take():
    pass



# ======================================================================
def update(tree: tuple, old_value: str, new_value: str) -> list:
    if tree is None:
        return []
    
    idx, left, right = tree
    key, value = TABLE[idx]

    # TODO 
    if find(tree, old_value):
        update(tree, old_value, new_value)

while True:
    old_value = input('수정할 값을 입력하세요: ')
    new_value = input('새로운 값을 입력하세요: ')
    result = update(BST, old_value, new_value)
    print(repr(result))
    print()

# ======================================================================
def range_query(tree: tuple, lo: str, hi: str) -> list:
    ''' 
    memo : 함수를 쓸 때 lo < hi가 되도록 짜주세요.
    '''
    if tree is None:
        return []
    
    idx, left, right = tree
    key, value = TABLE[idx]

    if key < lo:
        return range_query(right, lo, hi)
    elif key == lo:
        return [(key, value)] + range_query(right, lo, hi)
    elif lo < key < hi:
        return range_query(left, lo, hi) + [(key, value)] + range_query(right, lo, hi)
    elif key == hi:
        return range_query(left, lo, hi) + [(key, value)]
    else: # hi < key
        return range_query(left, lo, hi)


while True:
    lo = input('하한을 입력하세요: ')
    hi = input('상한을 입력하세요: ')
    result = range_query(BST, lo, hi)
    print(repr(result))
    print()
