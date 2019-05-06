# Time Complexity : O(kn)
# Where k is a constant representing the maximum number of digits for any given number in the data. 
# 요소 값을 명시적으로 비교하지 않아도 정렬할 수 있다.
# stable algorithm -> 자리수의 위치가 바뀌면 안된다. 14와 41은 서로 다른 수이기 때문에.

def find_digit(number, digit, base):
	return (number // base ** digit) % base


def counting_sort_with_digit(input_list, digit, base):
    B = [-1] * len(input_list)
    C = [0] * base # [0] * ((base -1) + 1)
    for item in input_list:
        C[find_digit(item, digit, base)] += 1

    for i in range(base - 1):
        C[i + 1] += C[i]

    for j in reversed(range(len(input_list))):
        B[C[find_digit(input_list[j], digit, base)] - 1] = input_list[j]
        C[find_digit(input_list[j], digit, base)] -= 1
    return B


from math import log

def radix_sort_msd(data, base=10):
    # 입력된 리스트 가운데 최대값의 자릿수 확인
    digit = int(log(max(data), base) + 1)
    # 자릿수 별로 counting sort
    for d in range(digit):
        data = counting_sort_with_digit(data, d, base)
    return data