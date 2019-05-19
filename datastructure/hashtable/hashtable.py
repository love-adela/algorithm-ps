from pearson_hash import pearson_hash

# Open Addressing
# 업데이트, 삭제, 삽입, 

class OpenAddressing:
    def __init__(self, size):
        self.size = size
        # self.size = len(random_table)
        self.hashtable = [None] * self.size
        self.bucket = [None] * self.size

    def put(self, key, value):
        initial_position = self.pearson_hash(key, table)
        i = initial_position
        j = 0

        if i == initial_position:
            break

        while True:
            if self.hashtable[i] == None:
                self.hashtable[i] = key
                self.bucket[i] = value
                return
            if self.hashtable[i] == key:
                self.bucket[i] = data
                return
            
            j += 1
            i = (initial_position + j) % self.size
    
    def get(self, key:str): #탐색
        initial_position = self.pearson_hash(key, table)
        i = initial_position
        j = 1
        while self.hashtable[i] != None:
            if self.hashtable[i] == key:
                return self.bucket[i]
            i = (initial_position + j) % self.size
            j += 1
            if i == initial_position:
                return None
        return None

    def print_hash_table(self):
        for i in range(self.size):
            print('{:4}'.format(str(self.hashtable[i])), ' ', end='')
        print()
        for i in range(self.size):
            print('{:4}'.format(str(self.hashtable[i])), ' ', end='')
        print()

hash_object = OpenAddressing(len(random_table))
hash_object.put(, hash)
hash_object.put(, hash)
hash_object.put(, hash)
hash_object.put(, hash)
hash_object.put(, hash)
hash_object.put(, hash)
hash_object.put(, hash)

print("탐색 결과":)
print('{}의 data = ', hash_object({}))
print('{}의 data = ', hash_object({}))
print('해쉬테이블:')
hash_table.print_table()
