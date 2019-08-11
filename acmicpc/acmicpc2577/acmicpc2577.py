product = 1
for _ in range(3):
    n = int(input())
    product *= n

for i in range(10):
    count = str(product).count(str(i))
    print(count)
