TABLE = [
    ("alice", 1),
    ("bob", 2),
    ("lisa", 17),
    ("rachael", 34),
]

ORDERED_LIST = []

# ===========================================
def add(arr:list, new_value:str, lo=0, hi=None) -> list:
    new_arr = add(arr, new_value)

    if lo < 0:
        raise ValueError('lo have to be non-negative')
    if hi is None:
        hi = len(arr)

    while lo < hi:
        mid = (lo + hi) // 2
        if new_value < arr[mid]:
            hi = mid
        else:
            lo = mid + 1

    arr.add(lo, new_value)

while True:
    new_value = input('새로 넣을 값을 입력하세요: ')
    result = add(ORDERED_LIST, new_value)
    print(repr(result))
    print()

def get_index(arr:list, value:str, lo=0, hi=None)->index:

    if lo < 0:
        raise ValueError('lo have to be non-negative')
    if hi is None:
        hi = len(arr)
    
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def get(arr:list, query: str) -> int:
    if arr is None:
        return add(arr, new_value)

    index = get_index(arr, query)
    if index != len(arr) and arr[index] == query:
        return arr[index]
    raise ValueError('No item found with this query')   

def delete(arr:list, query: str) -> list: 
    # TODO
    pass

def update():
    # TODO
    pass

def range_query():
   '''
   memo: 함수를 쓸 때 lo < hi 가 되도록 짜주세여.
   '''
   # TODO
   pass
