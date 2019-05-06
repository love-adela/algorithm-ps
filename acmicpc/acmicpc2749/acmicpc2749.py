# # pisano period : 
  # For any integer n, the sequence of Fibonacci numbers taken modulo n is periodic. 
  # 주기의 길이가 P면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.
  # M은 10 ** k 일 때, 주기는 항상 15 * 10 ** (k -1)이 된다.

# 문제 풀이 힌트 
  # 일관성을 잃지 않고 정의역 (Domain)을 확장시킬 것 => '해석적 확장' 
  # 행렬 곱 연산 활용하기

def pisano_period(n:int) -> int:
    fibo = [0, 1]
    quotient = 1000000
    period = int(quotient / 10 * 15)
    index = 2

    while index < period:
        fibo.append(fibo[index-1] + fibo[index-2])
        fibo[index] %= quotient
        index += 1
    return fibo[n%period]

n = int(input())
print(pisano_period(n))