class Trie:
    def __init__(self):
        self.children = [None] * 10
        self.is_matched = False

    def insert(self, key:str, index=0):
        if index == len(key):
            self.is_matched = True
        else:
            next_index = int(key[index])
            if self.children[next_index] == None:
                self.children[next_index] = Trie()
            self.children[next_index].insert(key, index + 1)

    def find(self, key:str, index=0):
        if index == len(key):
            return self
        next_index = int(key[index])
        if self.children[next_index] == None:
            return None
        return self.children[next_index].find(key, index + 1)

    def is_last_leaf(self) -> bool:
        if any([self.children[index] for index in range(10)]):
            return True
        return False

if __name__ == '__main__':
    for _ in range(int(input())):
        root = Trie()
        n = int(input())
        nums = [input().rstrip() for _ in range(n)]
        for num in nums:
            root.insert(num)
        flag = True

        for num in nums:
            if root.find(num).is_last_leaf():
                print('NO')
                flag = False
                break
        if flag:
            print('YES')
