import sys

def input_line():
    return sys.stdin.readline().strip()

class Trie:
    def __init__(self, key):
        self.node = {}
        self.key = key

    def insert(self, query):
        if self.node.get(query) is None:
            self.node[query] = Trie(0)
        return self.node[query]

N = int(input_line())
parent_trie = Trie(0)
children_trie = Trie(0)
bucket = {}

for i in range(1, N + 1):
    letter = input_line()
    parent = parent_trie
    children = children_trie
    teleportations = 0

    for j in range(len(letter)):
        parent = parent.insert(letter[j])
        children = children.insert(letter[len(letter) - j - 1])

        if parent.key == children.key:
            if bucket.get(parent.key) is None:
                bucket[parent.key] = 0
            teleportations = max(teleportations, bucket[parent.key] + 1)

    parent.key = children.key = i
    bucket[i] = teleportations
print(max(bucket.values()))
