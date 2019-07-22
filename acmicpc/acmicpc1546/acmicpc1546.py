n = int(input())
scores = list(map(int, input().split()))
maximum = max(scores)
new = [(lambda x: ((x / maximum) * 100))(x) for x in scores]
average = sum(new) / n
print(f'{average}')

