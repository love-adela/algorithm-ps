"""
j: 각 문자열에서 남겨놓을 맨 뒤 글자 수
seq: 끝 j글자만 남겼을 때 중복을 제외한 문자열 목록
n: 전체 문자열 개수
"""

N = int(input())
students = [input() for _ in range(N)]
length = len(students[0])

for j in range(1, length+1):
    seq = {student[-j:] for student in students}
    if len(seq) == N:
        print(j)
        break
