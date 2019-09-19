# Time Complexity : O(kn)
# Where k is a constant representing the maximum number of digits for any given number in the data. 
# 요소 값을 명시적으로 비교하지 않아도 정렬할 수 있다.
# stable algorithm -> 자리수의 위치가 바뀌면 안된다. 14와 41은 서로 다른 수이기 때문에.

def radix_lsd(input_list):
    position = 1

    while True:
        empty_lists = [list() for _ in range(10)]
        is_sorted = True

        for number in input_list:
            radix = number // position % 10
            empty_lists[radix].append(number)

            if number // position > 10:
                is_sorted = False

        position *= 10
        input_list.clear()

        for numbers in empty_lists:
                for num in numbers:
                    input_list.append(num)

        if is_sorted:
            return input_list
