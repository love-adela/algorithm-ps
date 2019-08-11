import random

USE_RANDOM_SEED = False

hash_table = [None for _ in range(20)]
look_up_table = [x for x in range(256)] 

if USE_RANDOM_SEED:
    random.Random(0).shuffle(lookup_table)
else:
    random.shuffle(lookup_table)


def pearson_hash(key:str) -> int:
    hash = 0
    for ch in key:
        hash = random_table[hash ^ (ord(ch) % 256)]
    return hash % len(hash_table)
