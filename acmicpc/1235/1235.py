N = int(input())
students = []
for _ in range(N):
    student = input()
    students.append(student)
length = len(students[0])

for j in range(1, length+1):
    seq = set()
    for i in range(N):
        item = students[i][-j:]
        seq.add(item)
    if len(seq) == N:
        print(j)
        break
