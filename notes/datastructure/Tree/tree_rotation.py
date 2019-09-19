def rotate_tree_clock_wise(tree: list) -> list:
    if tree is None:
        return None
    if tree[1] is None:
        return None
    # Invariant : tree = List
    _, left, right = tree
    return [left[0], left[1], [tree[0], left[2], right]]


def rotate_tree_counter_clock_wise(tree: list) -> list:
    if tree is None:
        return None
    if tree[2] is None:
        return None
    # Invariant : tree = List
    _, left, right = tree
    return [right[0], [tree[0], left, right[1]], right[2]]

print(rotate_tree_clock_wise([
    'd',
    ['b', ['a', None, None], ['c', None, None]],
    ['e', None, None],
]))

print(rotate_tree_counter_clock_wise([
    'b', 
    ['a', None, None], 
    ['d', ['c', None, None], ['e', None, None]]
]))