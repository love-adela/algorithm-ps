import random

to_sort = [(9 - len(bin(i))) * str(0) + bin(i)[2:] for i in range(128)]
random.shuffle(to_sort)

for i in range(6, -1, -1):
	empty_lists = [[], []]
	
	for j in range(len(to_sort)):
		if to_sort[j][i] == str(0):
			empty_lists[0].append(to_sort[j])
		else:
			empty_lists[1].append(to_sort[j])
	
	for j in range(64):
		for k in range(2):
			to_sort[k * 64 + j] = empty_lists[k][j]

print(to_sort)
