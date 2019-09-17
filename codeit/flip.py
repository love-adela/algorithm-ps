# Time Complexity : O(n ** 2)
def flip(some_list):
    return some_list if len(some_list) == 0 and 1 else some_list[-1:] + flip(some_list[:-1])

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)    