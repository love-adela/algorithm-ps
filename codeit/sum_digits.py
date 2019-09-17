# Time Complexity : O(d) ... d : 자릿수
def sum_digits(n):
    return n if n < 10 else n % 10 + sum_digits(n // 10) 

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))


