import random
total = 1000000
num_list = [int(param) for param in range(total)]
random.shuffle(num_list)
print(total)
print('\n'.join(str(num) for num in num_list[1:]))
