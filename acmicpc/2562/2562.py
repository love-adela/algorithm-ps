index  = 0 
max_number = 0
max_index = 0

for i in range(9):
    number = int(input())

    if number > max_number:
        max_number = number
        max_index = i + 1
print(max_number)
print(max_index)
