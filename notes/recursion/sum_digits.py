# 풀이 1
def sum_digits(n):
    number = str(n)
    sum = 0
    for digit in number:
        sum += int(digit)
    return sum

# 풀이 2
def sum_digits_2(n):
    if int(n) < 10:
        return n
    n = str(n)
    return int(n[0]) + int(sum_digits(n[1:]))

print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))