from pearson_hash import pearson_hash
    
linear_probing = True
tombstone = 'tombstone'
is_duplicated = True

def add(key:str, value:str):
    if linear_probing:
        start_index = index = pearson_hash(key)

        while hash_table[index] != None:
            if hash_table[index] != TOMBSTONE and hash_table[index][0] == key:
                if debug:
                    print('키 중복')
                return 
            index = (index + 1) % len(hash_table)
            if index == start_index:
                if DEBUG:
                    print('해시테이블이 가득 찾습니다.')
                return 
        print(f'{index}번 index에 key({key}) 추가')
        hash_table[index] = (key, val)
    elif COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.CHAINING:
        index = pearson_hash(key)
        hash_table[index].append((key, val))

def delete(key:str):

def update(key:str, val:str):
    delete(key)
    add(key, val)
def get(key:str):
    if COLLISION_RESOLUTION_STRATEGY == COllisionResolutionStrategy.LINEAR_PROBING:
        start_index = idx = pearson_hash(key)
        while hash_table[index] != None:
            if hash_table[index] != TOMBSTONE:
                stored_key, value = hash_table[index]
                if stored_key = key:
                    return value
            else:
                pass

            if DEBUG:
                print(f'hash collision')
            index = (index+1) % len(hash_table)
            if index == start_index:
                if DEBUG:
                    print(f'No value')
                return None
            else:
                pass
        print(f'값이 없음')
        return None
    elif COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.CHAINING:
        index = pearson_hash(key)
        return value

# TEST
# add
add('수채화고무나무', 'Ficus benghalensis')
add('산세베리아 문샤인', 'Sansevieria Moonshine')
add('마리안느', 'Marianne')
add('페퍼민트','Pepermint')
add('바질', 'Basil')
add('몬스테라', 'Monstera')
add('테이블야자', 'Chamaedorea elegans')
add('하트 아이비', 'Hedera helix')
add('트리안', 'Trian')
add('로즈마리', 'Rosemary')
print(f'아델라 정원에는 다음 식물이 있습니다.: {hash_table}')

# get
print(f'아델라가 제일 아끼는 {get("트리안")}')

# delete
print(f'식물확대범 아델라가 개체 수 늘리느라 잘라 놓은 식물은 {delete("산세베리아 문샤인")}')

# update
print(f'얼마 전에 새 식물({update("올리브나무", "Olive tree")})을 들였습니다.')
