from itertools import permutations
N = int(input())

word = []
for _ in range(N):
    word.append(input())
case = list(map(list, permutations(word, len(word))))

print(case)
answer = []
for item in case:
    palindrome = ''.join(item)
    if palindrome == palindrome[::-1]:
        answer.append(palindrome)

cnt = 0
for _ in range(len(answer)):
    cnt += 2 ** (len(word) -1) -1

for elem in word:
    if elem == elem[::-1]:
        cnt += 1
print(cnt)
