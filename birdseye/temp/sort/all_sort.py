input_numbers = [param for param in input().split()]
# Selection Sort
def selection_sort(unordered_numbers: list) -> list:
    print(f"원래 배열은 {input_numbers}")
    for i in range(len(unordered_numbers)):
        print(f"i = {i}일 때===========================")
        for j in range(len(unordered_numbers)):
            print(f"j = {j}일 때")
            if unordered_numbers[i] < unordered_numbers[j]:
                unordered_numbers[i], unordered_numbers[j] = unordered_numbers[j], unordered_numbers[i]
                print(unordered_numbers)
    return unordered_numbers
print(f"Selection Sort: {selection_sort(input_numbers)}")            