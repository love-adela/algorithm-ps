def binary_tree_list(r:int)->list:
    return [r, [], []]


def insert_left(root:list, new_node:int)->list:
    tree = root.pop(1)
    if len(tree) > 1:
        root.insert(1, [new_node, tree, []])
    else:
        root.insert(1, [new_node, [], []])
    return root


def insert_right(root:list, new_node:int)->list:
    tree = root.pop(2)
    if len(tree) > 1:
        root.insert(2, [new_node, tree, []])
    else:
        root.insert(2, [new_node, [], []]) 
    return root


def get_root(root:list)->int:
    return root[0]


def set_root(root:list, new_value)->int:
    root[0] = new_value 


def get_left_child(root:list)->list:
    return root[1]


def get_right_child(root:list)->list:
    return root[2]


r = binary_tree_list(3)
print(insert_left(r, 4))
print(insert_left(r, 5))
print(insert_left(r, 6))
print(insert_left(r, 7))
print(insert_left(r, 8))
print(insert_right(r, 6))
print(insert_right(r, 5))
print(insert_right(r, 4))
print(insert_right(r, 3))
print(insert_right(r, 2))
print(get_root(r))
print(get_left_child(r))
print(get_right_child(r))
