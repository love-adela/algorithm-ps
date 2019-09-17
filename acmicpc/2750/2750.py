# from random import randint
# example = []
# 계속 변수가 쓰이면 선언하고 아니면 바로 쓰기

# example = [randint(1, 1000) for x in range(0, 10001)]
# print(example)

# result = []
# for i in range(number):
#     result.append(int(input()))

# result = [int(input()) for _ in range(number)]
number = int(input())
example = [int(input()) for i in range(number)]


def indescending_bubble(sample_list):
    for i in range(len(sample_list)):
        iteration = 0
        for iteration in range(len(sample_list) - (1 + i)):
            if sample_list[iteration] > sample_list[iteration + 1]:
                sample_list[iteration], sample_list[iteration +1] = sample_list[iteration +1], sample_list[iteration]

    return sample_list


sorted_result = indescending_bubble(example)
str_result = []
for elem in sorted_result:
    str_result.append(str(elem))
print('\n'.join(str_result))