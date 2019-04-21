import random

class PearsonHasher:
    def __init__(self, length: int, seed):
        self.length = length
        generator = random.Random()
        generator.seed(seed)
        self.table = list(range(256))
        generator.shuffle(self.table)

    def hash(self, data):
        result = len(data) % 256
        for d in data:
            hash_result = self.table[(data[0] + d) % 256]
        return result
