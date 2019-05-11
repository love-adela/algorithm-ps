import random

table = [x for x in range(256)] # 해쉬값을 쓰기 위해서 랜덤하게 ㅇㅇ를 생성
# table = list(range(256))
random.shuffle(table) # 고정시키려면 seed 사용할 것

def pearson_hash(character:str, random_table:list) -> int:
    hash = len(character) % len(random_table) # 256 (어떤 값을 넣어도 % 연산을 했을 때, 결과값이 0 ~ 255로 나온다.)

    for i in character:
        hash = random_table[hash^ord(i)]
    return hash


# Test
print(pearson_hash(input("유니코드 코드 포인트로 변환하고 싶은 문자열을 입력하세요.\n"), table))
