# create hash table of size 10 with empty data
hash_table = [None] * 10
# print(hash_table)

def hashing(key):
    return key % len(hash_table)
 

def insert(hash_table, key, value):
    hash_key = hashing(key)
    hash_table[hash_key] = value     

# test
insert(hash_table, 10, 'Cat')
print(hash_table)
insert(hash_table, 25, 'Dog')
print(hash_table)


def update(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))


# test 
update(hash_table, 10, 'Cat')
print(hash_table)
update(hash_table, 25, 'Dog')
print(hash_table)
update(hash_table, 20, 'Hamster')


def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)    
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv 
        if key == k:
            key_exists = True 
            break
    if key_exists:
        del bucket[i]
        print(f'Key { key } deleted')
    else:
        print(f'Key { key } not found')
 
# test 
delete(hash_table, 100) # Key 100 not found
print (hash_table) 
delete(hash_table, 10)
print (hash_table)



