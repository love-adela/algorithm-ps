import random

look_up_table = [x for x in range(256)]
random.shuffle(table) # 고정시키려면 seed 사용할 것

def pearson_hash(character:str, random_table:list) -> int:
    hash = len(character) % len(random_table) 
    for i in character:
        hash = random_table[hash^ord(i)]
    return hash

# Test
print(pearson_hash(input("유니코드 코드 포인트로 변환하고 싶은 문자열을 입력하세요.\n"), table))
