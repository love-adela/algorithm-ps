def main(n):
    count, max_count = 1, 1
    radix = n[0]
    for l in n[1:]:
        if l == radix:
            count += 1
        else:
            max_count = max(count, max_count)
            radix = l
            count = 1
    max_count = max(count, max_count)
    return max_count

for _ in range(3):
    print(main(input()))
